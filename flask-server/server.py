#External Imports
from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS

#Standard Python Lib imports
import threading
import time
import logging

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

#activate logging
logging.basicConfig(filename = 'Serverlog.log', level = logging.DEBUG)


#internal functions for WebSocket-Handshake
@socketio.on("connect")
def connected():
    app.logger.info(request.sid)
    app.logger.info("client has connected")
    emit("connect",f"user {request.sid} connected")

@socketio.on("disconnect")
def disconnected():
    app.logger.info("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected")

#internal Functions
@app.route("/data")
def uploadData():
    global data
    data = createWordCountMap()
    if not data:
        pass
    else:
        app.logger.info("New Data is uploaded")
        socketio.emit("newData",{"wordcountmap" : data})
        return {"wordcountmap" : data}

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
        app.logger.info("Received data is corrupted")
        return False
    if latestDateArticle != latestDateData:
        latestDateData = latestDateArticle
        return True
    else:
        return False
    
def updateDataThread(updatedelay = 5):
    while True:
        b_isNewData = isNewData()
        if b_isNewData != "Error" and b_isNewData:
            uploadData()
        time.sleep(updatedelay)


# main
if __name__ == '__main__':
    update_data_thread = threading.Thread(target=updateDataThread)
    update_data_thread.setDaemon(True)
    update_data_thread.start()
    socketio.run(app, debug=True,port=5001)