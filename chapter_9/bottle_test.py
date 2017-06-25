import requests

response = requests.get('http://localhost:9999/echo/我操！')
if response.status_code == 200:
	print(response.text)
