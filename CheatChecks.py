import math
def CheatChecks(file):
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
    replay = file           #lets user input replay .txt
    replayFile = open(replay,'rt')
    print(f"Now reviewing {file}")
    for line in replayFile:                   #appends each line into seperate elements of list(lines)
        lines.append(line)
    str = lines[0]       #checks if the map is played with Doubletime.
    DTcheck = str.find('DoubleTime',0)
    for useless in range(0,11):           #pops the useless 11 lines of pre-info
        lines.pop(0)
    for element in lines: #fishes lines out for x,y coordinates and stores them in lists(xCoord&yCoord)
        str=element
        index = str.find(substr,0) + 3
        index2 = str.find(substr2,0)
        xTemp = element[index:index2]
        xCoord.append(xTemp)
        index2+=1
        index3 = str.find(substr3,index2)
        yTemp = element[index2:index3]
        yCoord.append(yTemp)
    xCoord = [float(i) for i in xCoord]   #converts list of str to list of float for calculations
    yCoord = [float(i) for i in yCoord]
    linearInstances = 0
    slopeValue = 0
    slopeValue2 = 0
    cheatFlags = 0
    ################################################################################
    #calculates slopes if cursor is moving in same direction for two instances
    #if so, the slopes are compared to see if it moves linearly
    ################################################################################
    if DTcheck != -1:
        for value in range(0,len(xCoord)-4,4):
            if (xCoord[value]-xCoord[value+2])<0 and (xCoord[value+2]-xCoord[value+4])<0:
                if (yCoord[value]-yCoord[value+2])<0 and (yCoord[value+2]-yCoord[value+4])<0:
                    slopeValue = (yCoord[value+2]-yCoord[value])/(xCoord[value+2]-xCoord[value])
                    slopeValue2 = (yCoord[value+4]-yCoord[value+2])/(xCoord[value+4]-xCoord[value+2])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:  #+1 and -1 for slope calculaction leniency
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+2])<0 and (xCoord[value+2]-xCoord[value+4])<0:
                if (yCoord[value]-yCoord[value+2])>0 and (yCoord[value+2]-yCoord[value+4])>0:
                    slopeValue = (yCoord[value+2]-yCoord[value])/(xCoord[value+2]-xCoord[value])
                    slopeValue2 = (yCoord[value+4]-yCoord[value+2])/(xCoord[value+4]-xCoord[value+2])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+2])>0 and (xCoord[value+2]-xCoord[value+4])>0:
                if (yCoord[value]-yCoord[value+2])>0 and (yCoord[value+2]-yCoord[value+4])>0:
                    slopeValue = (yCoord[value+2]-yCoord[value])/(xCoord[value+2]-xCoord[value])
                    slopeValue2 = (yCoord[value+4]-yCoord[value+2])/(xCoord[value+4]-xCoord[value+2])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+2])>0 and (xCoord[value+2]-xCoord[value+4])>0:
                if (yCoord[value]-yCoord[value+2])<0 and (yCoord[value+2]-yCoord[value+4])<0:
                    slopeValue = (yCoord[value+2]-yCoord[value])/(xCoord[value+2]-xCoord[value])
                    slopeValue2 = (yCoord[value+4]-yCoord[value+2])/(xCoord[value+4]-xCoord[value+2])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            else:
                linearInstances = 0
            if linearInstances >= 2:    #adds to cheat flags for suspicious cursor movment
                cheatFlags+=1
                linearInstances = 0
    else:
        for value in range(0,len(xCoord)-6,6):
            if (xCoord[value]-xCoord[value+3])<0 and (xCoord[value+3]-xCoord[value+6])<0:
                if (yCoord[value]-yCoord[value+3])<0 and (yCoord[value+3]-yCoord[value+6])<0:
                    slopeValue = (yCoord[value+3]-yCoord[value])/(xCoord[value+3]-xCoord[value])
                    slopeValue2 = (yCoord[value+6]-yCoord[value+3])/(xCoord[value+6]-xCoord[value+3])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:  #+1 and -1 for slope calculaction leniency
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+3])<0 and (xCoord[value+3]-xCoord[value+6])<0:
                if (yCoord[value]-yCoord[value+3])>0 and (yCoord[value+3]-yCoord[value+6])>0:
                    slopeValue = (yCoord[value+3]-yCoord[value])/(xCoord[value+3]-xCoord[value])
                    slopeValue2 = (yCoord[value+6]-yCoord[value+3])/(xCoord[value+6]-xCoord[value+3])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+3])>0 and (xCoord[value+3]-xCoord[value+6])>0:
                if (yCoord[value]-yCoord[value+3])>0 and (yCoord[value+3]-yCoord[value+6])>0:
                    slopeValue = (yCoord[value+3]-yCoord[value])/(xCoord[value+3]-xCoord[value])
                    slopeValue2 = (yCoord[value+6]-yCoord[value+3])/(xCoord[value+6]-xCoord[value+3])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            elif (xCoord[value]-xCoord[value+3])>0 and (xCoord[value+3]-xCoord[value+6])>0:
                if (yCoord[value]-yCoord[value+3])<0 and (yCoord[value+3]-yCoord[value+6])<0:
                    slopeValue = (yCoord[value+3]-yCoord[value])/(xCoord[value+3]-xCoord[value])
                    slopeValue2 = (yCoord[value+6]-yCoord[value+3])/(xCoord[value+6]-xCoord[value+3])
                    if slopeValue<= slopeValue2+0.03 and slopeValue>=slopeValue2-0.03:
                        linearInstances+=1
            else:
                linearInstances = 0
            if linearInstances >= 2:    #adds to cheat flags for suspicious cursor movment
                cheatFlags+=1
                linearInstances = 0
    songLengthSearch = lines[-1]     #determine allowed amount of flags based on song length.
    str = lines[-1]
    flagdex = 0
    flagdex = str.find('(',0)
    songLength = songLengthSearch[0:flagdex]
    if DTcheck != -1:
        songLength = int(songLength)/1.5
    cheatFlagLeniency = int(songLength)/4000
    if cheatFlags > cheatFlagLeniency:
        print(f"Wow! This replay has {cheatFlags} cheat flags for linear movement! That replay is definitely cheated!")
    else:
        print("No cheats have been detected in linear movement!")
    ################################################################################
    #counts the number of times a cursor moves>150pixels in one instance
    ################################################################################
    teleportInstances = 0

    for value in range(0, len(xCoord) - 1):
        if math.sqrt(pow(xCoord[value + 1] - xCoord[value], 2) + pow(yCoord[value + 1] - yCoord[value], 2)) > 150:
            teleportInstances += 1
    print("Number of cursor teleports: ", teleportInstances)
    if teleportInstances>30:
        print("That's a suspicious amount of cursor teleports! This play might be cheated!")
    ################################################################################
    #Cursor Acceleration
    ################################################################################
    secAccelDev = []
    accelDev = []
    acceleration = []
    totalAccel = 0
    sectAccelDev = 0
    totalSecAccelDev = 0
    averageDeviation = 0
    sectLen = len(xCoord)/100        #divides number of coordinates by 100 to section them in 100 pieces
    for section in range(1,100):     #values from 1,100
        for val in range(0,int(sectLen*section)):   #values from 0 to 1/100 of # of coordinates MULTIPLY by section number piece
            acceleration.append(accelCalc(val, xCoord, yCoord))   #appends acceleration value from accelCalc function
        acceleration = [float(i) for i in acceleration]  #turns accel list of str to list of int
        for i in range(0,len(acceleration)-1):             #for loop to go through list of int acceleration
            accelDev.append(acceleration[i+1]-acceleration[i])   #appends the subtracted acceleration (deviation) to accelDev
        accelDev = [float(i) for i in accelDev]   #turns accelDev list from list of str to list of int
        for stuff in accelDev:   #for loop to add together all values of accelDev
            totalAccel+=abs(stuff) #abs because accelDev may be negative from subtraction
        secAccelDev.append(totalAccel/len(accelDev))    #divides totalAccel to get the section's average acceleration deviation
        acceleration = []       #resets acceleration list
        accelDev = []           #resets accelDev list
    secAccelDev = [float(i) for i in secAccelDev]     #turns setAccelDev list of str to list of int
    for i in range(0,len(secAccelDev)):                  #goes through elements of secAccelDev
        totalSecAccelDev+=secAccelDev[i]                #adds total of all sections of average acceleration deviation
    averageDeviation = totalSecAccelDev/len(secAccelDev)          #takes the total average acceleration deviation of all sections.
    averageDeviation = "{0:.2f}".format(averageDeviation)
    print(f"The average acceleration deviation of the map is: {averageDeviation}!")
    if DTcheck != -1:
        if float(averageDeviation)<200:
            print("That's an unusually steady acceleration! This play may be suspicious.")
        if float(averageDeviation)>350:
            print("That's an unusually unstable acceleration! This play may be suspicious.")
    else:
        if float(averageDeviation)>250:
            print("That's an unusually unstable acceleration! This play may be suspicious.")
    replayFile.close()
def accelCalc(val: int, xCoord: list, yCoord:list) -> int:
    """calculate acceleration of a given instance
    """
    accelValue = math.sqrt(pow(xCoord[val+1]-xCoord[val],2)+pow(yCoord[val+1]-yCoord[val],2))
    return accelValue
