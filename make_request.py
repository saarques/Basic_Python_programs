import requests

BASE_URL = "http://127.0.0.1:8085/"
dope = {"address" : "cell.bmp"}

response = requests.post("{}/predict".format(BASE_URL), json = dope)

response.json()