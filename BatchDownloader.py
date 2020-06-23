from six.moves import urllib
 
infile = open("Cryptic_Fiction.m3u", "r")
   
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

    urb = "download" + str(y)
    ur3 = '/Users/mysti/Downloads/' + urb + ".mp3"

    urllib.request.urlretrieve(ur, ur3)



  
