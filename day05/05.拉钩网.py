import requests
import jsonpath

url=''

response=requests.get(url)
data=response.json()
jsonpath.jsonpath()