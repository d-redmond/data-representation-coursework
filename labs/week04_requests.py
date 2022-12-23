# import requests
# url = "http://google.com"
# response = requests.get(url)
# print(response.text)

import requests
URL = http://andrewbeatty1.pythonanywhere.com/books
response = requests.get(URL)
print(response.json())

def readbooks():
    response = requests.get(URL)
    return response.json()
if__name__=="__main__":
    print(readbooks())

def readbooks(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


