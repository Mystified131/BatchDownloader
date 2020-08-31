import requests
import urllib.request
import re
from bs4 import BeautifulSoup
from subprocess import call

infile = open("ThisAMURL.txt", "r")
   
contentpg = []

astr = ""

plist = infile.readline()
while plist:
    astr = plist.strip()
    contentpg.append(astr)
    plist = infile.readline()

infile.close()

mussrl = []

i = 0

for elem in contentpg:

    try:
        r = requests.get(elem)
        soup = BeautifulSoup(r.content, 'html.parser')
        for a in soup.find_all('a', href=re.compile('http.*.mp3')):
            i=i+1
            print("Check: ", i)
            url = a['href']
            file=url.split()[0]
            mussrl.append(str(file))
           

    except: 
        print("Error for URL: ", elem)

print(mussrl)

outfile = open("ThisAmericanLife.txt", "w")

for elem in mussrl:
    outfile.write(elem + '\n')

outfile.close()

call(["python", "TALDownloader.py"])




