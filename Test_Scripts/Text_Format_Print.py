from numpy.ma.core import append

strand = "AAAAAGTAGTAGATGATGAATGCTACGTATCGACGGGCGACGTATGATGCTGAGGATCGATGCATGCTCGATGAGCTGCGCTGAGCATCTAGCTATGCTAGCTATCGTAGCA"
#strand is a string#.

count =0
vcount = 0
finalArray = [] #this is the array that must contain the format.
tempArray = []
message = []
lower = 0
upper = 0

for x in strand:
    count += 1
    vcount += 1
    tempArray.append(x)
    if count == 60 or vcount == len(strand):
        count = 0
        finalArray.append("".join(tempArray))
        tempArray = []
    else: continue

for x in range(0,len(finalArray)):
    lower = upper+1
    upper = upper + len(finalArray[x])
    if len(strand) > 60:
        temp = f"{lower}-, {strand},-{upper}"
        message.append(temp)

    elif len(strand) < 60:
        temp = f"{lower}-, {strand},-{upper}"
        message.append(temp)

lower = 0
upper = 0

print(message)