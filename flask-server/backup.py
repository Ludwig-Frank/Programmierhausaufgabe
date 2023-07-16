from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
import threading
import time
import datainterface
import reduce
import map

global latestDateData
global data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,ping_timeout = 5,cors_allowed_origins="*", )

latestDateData = 0 
data = []

def updateData(updatedelay = 10):
    global data
    while True:
        if isNewData():
            uploadData()
        time.sleep(updatedelay)

@app.route("/members")
def uploadData():
    global data
    data = createWordCountMap()
    if not data:
        return {"wordcountmap" : "Error while loading data"}
    else:
        print("Daten werden gesendet")
        socketio.emit("newData", {"wordcountmap":data})
        return {"wordcountmap" : data}

def createWordCountMap():
    retVal = []
    articles = datainterface.getArticleData()
    if not articles:
        return False
    for article in articles:
        wordCountMap = map.mapper(article[1])
        wordCountMap = reduce.reducer(wordCountMap)
        wordCountList = createMemberlist(wordCountMap)
        retVal.append([article[0], wordCountList])
    return retVal

def createMemberlist(list):
    newList = []
    for data in list:
        member = data[0] + " : " + str(data[1])
        newList.append(member)
    return newList

def isNewData():
    return True
    global latestDateData
    latestDateArticle = datainterface.getLatestArticleDate()
    if not latestDateArticle:
        return "Error"
    if latestDateArticle != latestDateData:
        latestDateData = latestDateArticle
        return True

if __name__ == '__main__':
    update_data_thread = threading.Thread(target=updateData)
    update_data_thread.setDaemon(True)
    update_data_thread.start()
    socketio.run(app, debug=True,port=5003)