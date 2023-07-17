import requests
import html2text

#global variables
url = "https://www.thekey.academy/wp-json/wp/v2/posts?per_page=100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

#Returns Title and content of the articles listed on the url
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
        element["content"] = html2text.html2text(htmltext)
        retVal.append(element)
    return retVal

# returns the publication date of the newest article from the url
def getLatestArticleDate():
    try:
        response = requests.get(url, headers=headers)
    except Exception:
        print("Request failed")
        return False
    if  response.status_code != 200:
        print("response code was not 200")
        return False
    try:
        response_json = response.json()
    except Exception:
        print("Json tranform did not work")
        return False
    return response_json[0]['date']
    



if __name__ == "__main__":
    articledata = getArticleData()
    latestArticleDate = getLatestArticleDate()
    print(type(latestArticleDate))