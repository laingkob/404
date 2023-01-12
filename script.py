import requests

url = "http://webdocs.cs.ualberta.ca/~hindle1/1.py"
r = requests.get(url, allow_redirects=True)
print(r.text)

