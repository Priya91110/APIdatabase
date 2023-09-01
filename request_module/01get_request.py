# import requests
# resp = requests.get("https://api.github.com/events")
# # print(resp.status_code)
# # print(resp.headers['content-type'])
# # print(resp.encoding)
# print(resp.text)
# print(resp.json())

import requests
url ="https://api.github.com/events"
resp = requests.get(url)
print(resp.json())