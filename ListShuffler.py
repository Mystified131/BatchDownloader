#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
   

contents = []

srchstr = 'C:\\Users\\mysti\\Coding\\BatchDownloader\\'

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".m3u"):

            contents.append(filepath)

pl1 = []
pl2 = []
pl3 = []
pl4 = []
pl5 = []


for elem in contents:

    infile = open(elem, "r")

    plist = infile.readline()

    while plist:
        pl1.append(plist.strip())
        plist = infile.readline()
        pl2.append(plist.strip())
        plist = infile.readline()
        pl3.append(plist.strip())
        plist = infile.readline()
        pl4.append(plist.strip())
        plist = infile.readline()
        pl5.append(plist.strip())
        plist = infile.readline()

    infile.close()

finpl = []

for elem in pl1:
    if elem not in finpl:
        finpl.append(elem)

for elem2 in pl2:
    if elem2 not in finpl:
        finpl.append(elem2)

for elem3 in pl3:
    if elem3 not in finpl:
        finpl.append(elem3)

for elem4 in pl4:
    if elem4 not in finpl:
        finpl.append(elem4)

for elem5 in pl5:
    if elem5 not in finpl:
        finpl.append(elem5)

oustr = "Shuffled_Playlist.txt"

outfile = open("temp.txt", "w")

for elem in finpl:
    outfile.write(elem + '\n')

outfile.close()       

outfile = open(oustr, "w")

with open("temp.txt") as f: 
    for line in f: 
        if not line.isspace(): 
            #sys.stdout.write(line)
            outfile.write(line)

outfile.close()

## THE GHOST OF THE SHADOW ##




