import bs4
from bs4 import BeautifulSoup, ResultSet
from bs4 import element
import requests
import re

html = requests.get("http://www.pythonscraping.com/pages/page1.html")
content = html.text
bsObj: BeautifulSoup = BeautifulSoup(content, features="lxml")
print(bsObj.h1)

html: requests.Response = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
content = html.text
# print(content)
bsObj = BeautifulSoup(content, features="lxml")

nameList: ResultSet = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    name = name
    """:type : bs4.element.Tag"""
    print(name.get_text())

html: requests.Response = requests.get("http://www.pythonscraping.com/pages/page3.html")
content = html.text
bsObj = BeautifulSoup(content, features="lxml")
imageList: ResultSet = bsObj.findAll("img", {"src": re.compile("\.\./img/gifts/img.*\.jpg")})
for image in imageList:
    print(image.attrs["src"])
