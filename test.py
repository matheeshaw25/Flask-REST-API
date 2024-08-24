import requests # lets us send requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/bill") #send a get request to the url -> BASE+helloworld
print(response.json())


