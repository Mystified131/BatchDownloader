from six.moves import urllib
import os
 
print("")

dlist = input("Please enter the full file name of the text file to use as reference for downloads: ")

infile = open(dlist, "r")
   
contents = []

plist = infile.readline()
while plist:
    contents.append(plist)
    plist = infile.readline()
infile.close()

x = len(contents)

for y in range(x):

    ur = contents[y]

    print("")
    print("Downloading mp3 from: " + ur)

    filnam = os.path.basename(ur)

    filnm = 'This_American_Life_' + filnam.strip()

    ur3 = 'C:\\Users\\mysti\\Downloads\\' + filnm

    urllib.request.urlretrieve(ur, ur3)



  
