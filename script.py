import requests

url = "https://raw.githubusercontent.com/laingkob/404/lab1/script.py"
r = requests.get(url, allow_redirects=True)
print(r.text)

