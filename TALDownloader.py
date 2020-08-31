from six.moves import urllib
import os
 

infile = open("ThisAmericanLife.txt", "r")
   
contents = []

plist = infile.readline()
while plist:
    contents.append(plist)
    plist = infile.readline()
infile.close()

x = len(contents)

for y in range(x):

    try:

        ur = contents[y]

        print("")
        print("Downloading mp3 from: " + ur)

        filnam = os.path.basename(ur)

        filnm = 'This_American_Life_' + filnam.strip()

        ur3 = 'C:\\Users\\mysti\\Downloads\\' + filnm

        urllib.request.urlretrieve(ur, ur3)

    except:

        print("Download failed for: ", ur)

print("")

print("Downloads finished, please check your downloads folder.")


  
