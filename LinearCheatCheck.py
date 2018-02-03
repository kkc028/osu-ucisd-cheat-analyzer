xCoord=[]
yCoord=[]
lines = []
index=0
index2=0
index3=0
substr = ':'
substr2 = ','
substr3 = ')'
xTemp=0
yTemp=0
replay = input("Enter name of replay: ")
replayFile = open(replay,'rt')
for line in replayFile:
    lines.append(line)
for useless in range(0,11):
    lines.pop(0)
for element in lines:
    str=element
    index = str.find(substr,0) + 3
    index2 = str.find(substr2,0)
    xTemp = element[index:index2]
    xCoord.append(xTemp)
    index2+=1
    index3 = str.find(substr3,index2)
    yTemp = element[index2:index3]
    yCoord.append(yTemp)
for things in range(0,100):
    print(xCoord[things])
print(yCoord[0])
