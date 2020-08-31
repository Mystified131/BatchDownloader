import requests
import urllib.request
import re
from bs4 import BeautifulSoup
i=0
r = requests.get('https://www.thisamericanlife.org/715/long-awaited-asteroid-finally-hits-earth')
soup = BeautifulSoup(r.content, 'html.parser')
for a in soup.find_all('a', href=re.compile('http.*\.mp3')):
    i=i+1
    url = a['href']
    file=url.split()[0]
    ur3 = 'C:\\Users\\mysti\\Downloads\\test.mp3'
    print(file)
    urllib.request.urlretrieve(url, ur3)




