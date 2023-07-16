#External Imports
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS

#Standard Python Lib imports
import threading
import time
import json

#Internal Imports
import datainterface
import reduce
import map

#global variables 
global latestDateData
global data
latestDateData = 0 
data = []

# init for flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*", async_mode='threading')

#internal functions for WebSocket
def updateDataThread(updatedelay = 5):
    while True:
        b_isNewData = isNewData()
        if b_isNewData != "Error" and b_isNewData:
            uploadData()
        time.sleep(updatedelay)

@socketio.on("connect")
def connected():
    print(request.sid)
    print("client has connected")
    #emit("connect",json.dumps({'data':f"id: {request.sid} is connected"}))

@socketio.on("disconnect")
def disconnected():
    print("user disconnected")
    #emit("disconnect",f"user {request.sid} disconnected")

#internal Functions
def uploadData():
    global data
    data = createWordCountMap()
    if not data:
        pass
    else:
        print("New Data is uploaded")
        socketio.emit("newData",data)

def createWordCountMap():
    retVal = []
    articles = datainterface.getArticleData()
    if not articles:
        return False
    for article in articles:
        wordCountMap = map.mapper(article["content"])
        wordCountMap = reduce.reducer(wordCountMap)
        wordCountList = createMemberlist(wordCountMap)
        retVal.append([article["title"], wordCountList])
    return retVal

def createMemberlist(list):
    newList = []
    for data in list:
        member = data[0] + " : " + str(data[1])
        newList.append(member)
    return newList

def isNewData():
    global latestDateData
    latestDateArticle = datainterface.getLatestArticleDate()
    if not latestDateArticle:
        print("Received data is corrupted")
        return False
    if latestDateArticle != latestDateData:
        latestDateData = latestDateArticle
        return True
    else:
        return False

# main
if __name__ == '__main__':
    update_data_thread = threading.Thread(target=updateDataThread)
    update_data_thread.setDaemon(True)
    update_data_thread.start()
    socketio.run(app, debug=False,port=5001)