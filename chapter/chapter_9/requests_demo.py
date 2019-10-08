import requests

url = 'http://app.gushiwen.org/api/search2.aspx?type=guwen&token=gswapi&page=1&value=%E7%99%BD'
resp = requests.get(url)
print(resp)

print(resp.headers)
print(resp.text)
