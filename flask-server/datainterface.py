import requests
import html2text
url = "https://www.thekey.academy/wp-json/wp/v2/posts?per_page=100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def getArticleData():
    retVal = []
    try:
        response = requests.get(url, headers=headers)
    except Exception:
        return False
    if  response.status_code != 200:
        return False
    try:
        response_json = response.json()
    except Exception:
        return False
    for article in response_json:
        element = {
            "title" : "",
            "content" : ""
        }
        element["title"] = article['title']['rendered']
        htmltext = article['content']['rendered']
        element["text"] = html2text.html2text(htmltext)
        retVal.append(element)
    return retVal
    
def getLatestArticleDate():
    try:
        response = requests.get(url, headers=headers)
    except Exception:
        return False
    if  response.status_code != 200:
        return False
    try:
        response_json = response.json()
    except Exception:
        return False
    return response_json[0]['date']
    



if __name__ == "__main__":
    #articles = getArticlesAsString()
    getLatestArticleDate()