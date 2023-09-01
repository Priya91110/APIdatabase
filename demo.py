import requests
import json
response=requests.get('https://api.publicapis.org/entries')
print(response.status_code)
print(response.json())

# description=response.json()['results'][0]['description']
# print(description)


