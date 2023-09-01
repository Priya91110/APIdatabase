import requests    
from bs4 import BeautifulSoup
import json
url="https://www.codewithharry.com/blogpost/django-cheatsheet/"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

for heading in soup.find_all("h2"):
    print(heading.text)