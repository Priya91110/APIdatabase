import requests
url ="https://www.codewithharry.com"
resp = requests.get(url)
print(resp.text)
# for webscriping
with open("index.html", "w") as f:
    f.write(resp.text)