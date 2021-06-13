import requests

url = 'http://127.0.0.1:5000/getsetu'
def getSetu():
    req = requests.get(url)
    return req.json()