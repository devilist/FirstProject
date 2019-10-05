#! /usr/bin/env python3

import urllib.request as ur

url = 'http://www.baidu.com'

conn = ur.urlopen(url)
data = conn.read()
status = conn.status
contentType = conn.getheader('Content-Type')
print(status)
print(contentType)
for key, value in conn.getheaders():
    print(key, ':', value)
# print(data)
