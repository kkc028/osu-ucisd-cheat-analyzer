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
xCoord = [float(i) for i in xCoord]
yCoord = [float(i) for i in yCoord]
linearInstances = 0
slopeValue = 0
slopeValue2 = 0
for value in range(0,len(xCoord)-1):
    if (xCoord[value]-xCoord[value+1])<0 and (xCoord[value+1]-xCoord[value+2])<0:
        if (yCoord[value]-yCoord[value+1])<0 and (yCoord[value+1]-yCoord[value+2])<0:
            slopeValue = (yCoord[value+1]-yCoord[value])/(xCoord[value+1]-xCoord[value])
            slopeValue2 = (yCoord[value+2]-yCoord[value+1])/(xCoord[value+2]-xCoord[value+1])
            if slopeValue==slopeValue2:
                linearInstances+=1
    elif (xCoord[value]-xCoord[value+1])<0 and (xCoord[value+1]-xCoord[value+2])<0:
        if (yCoord[value]-yCoord[value+1])>0 and (yCoord[value+1]-yCoord[value+2])>0:
            slopeValue = (yCoord[value+1]-yCoord[value])/(xCoord[value+1]-xCoord[value])
            slopeValue2 = (yCoord[value+2]-yCoord[value+1])/(xCoord[value+2]-xCoord[value+1])
            if slopeValue==slopeValue2:
                linearInstances+=1
    elif (xCoord[value]-xCoord[value+1])>0 and (xCoord[value+1]-xCoord[value+2])>0:
        if (yCoord[value]-yCoord[value+1])>0 and (yCoord[value+1]-yCoord[value+2])>0:
            slopeValue = (yCoord[value+1]-yCoord[value])/(xCoord[value+1]-xCoord[value])
            slopeValue2 = (yCoord[value+2]-yCoord[value+1])/(xCoord[value+2]-xCoord[value+1])
            if slopeValue==slopeValue2:
                linearInstances+=1
    elif (xCoord[value]-xCoord[value+1])>0 and (xCoord[value+1]-xCoord[value+2])>0:
        if (yCoord[value]-yCoord[value+1])<0 and (yCoord[value+1]-yCoord[value+2])<0:
            slopeValue = (yCoord[value+1]-yCoord[value])/(xCoord[value+1]-xCoord[value])
            slopeValue2 = (yCoord[value+2]-yCoord[value+1])/(xCoord[value+2]-xCoord[value+1])
            if slopeValue==slopeValue2:
                linearInstances+=1
    else:
        linearInstances = 0
