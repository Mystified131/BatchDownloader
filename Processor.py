infile = open("ThisAmLife.txt", "r")
   
contents = []

astr = ""

plist = infile.readline()
while plist:
    if "Episode" in plist:
        astr = plist.strip()
        contents.append(astr)
    plist = infile.readline()
infile.close()

print(contents)

contentb = []

for elem in contents:
    anum = (elem.find("Episode"))
    bnum = anum + 7
    astr = elem[bnum:]
    substr = ""
    for elem2 in astr:
        if elem2.isalnum() or elem2 == " ":
            substr += (elem2)
    contentb.append(substr)

contentb1 = []
contentb2 = []

for elem in contentb:
    substr1 = ""
    for elem2 in elem:
        anum = (elem.find(elem2))
        if elem2.isnumeric() and anum < 5:
            substr1 += elem2
    contentb1.append(substr1)

print(contentb1)

contnum = []

for x3 in contentb1:
    astr = x3[:3]
    contnum.append(astr)

print(contnum)

conna = []

for v2 in contents:
    cnum = (v2.find(' "')) + 2
    v3 = v2[cnum:-1].lower()
    conna.append(v3)

print(conna)

conner = []

for elem in conna:
    substr3 = ""
    for elem2 in elem:
        if elem2 != " " and  elem2 != "!" and  elem2 != "?" and  elem2 != "," and elem2 != "." and elem2 != "'" and elem2 != "'" and elem2 != ":" and elem2 != ";":
            substr3 += elem2
        if elem2 == " ":
            substr3 += "-"
    conner.append(substr3)


print(conner)

ll = len(contentb1)

finst = []

for y4 in range(ll):
    finstr = "https://www.thisamericanlife.org/" + contentb1[y4] + "/" + conner[y4]
    finst.append(finstr)

print(finst)

outfile = open("ThisAMURL.txt", "w")

for elem in finst:
    outfile.write(elem + '\n')

outfile.close()



