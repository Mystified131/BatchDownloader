astr = "https://www.podtrac.com/pts/redirect.mp3/dovetail.prxu.org/188/917067fd-8b50-4e8b-8d29-6954e6e677e6/"

content = []

for x in range(715):
    y = str(x + 1) 
    y2 = y + ".mp3"
    y3 = astr + y2
    content.append(y3)

print(content)

outfile = open("ThisAmericanLife.txt", "w")

for elem in content:
    outfile.write(elem + '\n')

outfile.close()