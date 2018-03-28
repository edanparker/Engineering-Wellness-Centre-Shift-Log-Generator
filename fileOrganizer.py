import csv

#read in csv file to matrix 'data'
data = list(csv.reader(open('EWCForm_TestData.csv')))

#function that iterates through 'data' matrix and makes two new lists with pertinent information for graphing
def makeGraphData(yAxisIn, graphType):
    #plots a given year against time
    if yAxisIn == "first" or yAxisIn == "second" or yAxisIn == "third" or yAxisIn == "fourth" or yAxisIn == "fifth":
        #init
        xAxis = []
        xAxisTemp = readTimeIn(data)
        yAxis = []
        yAxisTemp = []
        
        #selection structure to interpret string input into values for indexing data matrix
        if yAxisIn == "first":
            yAxisTemp = sumYears(data, 13, "First Year")
        elif yAxisIn == "second":
            yAxisTemp = sumYears(data, 12, "Second Year")
        elif yAxisIn == "third":
            yAxisTemp = sumYears(data, 11, "Third Year")
        elif yAxisIn == "fourth":
            yAxisTemp = sumYears(data, 10, "Fourth Year")
        elif yAxisIn == "fifth":
            yAxisTemp = sumYears(data, 9, "Fifth Year")
    
        mymatrix = consolidateEntries(xAxisTemp,yAxisTemp)
        
        #split mymatrix into 1d lists yAxis and xAxis
        yAxis = mymatrix[0]
        xAxis = mymatrix[1]
        
        #print out lists to test functionality
        print(yAxis)
        print(xAxis)

    #plots the respective sums of all years in a pie or bar chart
    elif yAxisIn == "allYears":
        xAxis = readTimeIn(data)
        yAxis = [["Fifth","Fourth","Third","Second","First","Unknown"]]
        yAxisTemp = [0,0,0,0,0,0]
        for i in data[1:]:
            for j in range(0,6):
                sum = 0
                for k in range(0,8):
                    index = (j+9) + 6*k
                    if i[index]:
                        sum += int(i[index])
                yAxisTemp[j] += sum
        yAxis.append(yAxisTemp)
        print(yAxis)

    #plots a given discipline against time
    elif yAxisIn == "apple" or yAxisIn == "chemEng" or yAxisIn == "civil" or yAxisIn == "comp" or yAxisIn == "elec" or yAxisIn == "engPhys" or yAxisIn == "geo" or yAxisIn == "mining":
        xAxis = []
        xAxisTemp = readTimeIn(data)
        yAxis = []
        yAxisTemp = []
        #selection structure to interpret string input into values for indexing data matrix
        if yAxisIn == "Apple":
            yAxisTemp = sumDisciplines(data, 9, "Applied Mathematics and Engineering")
        elif yAxisIn == "ChemEng":
            yAxisTemp = sumDisciplines(data, 15, "Chemical Engineering")
        elif yAxisIn == "Civil":
            yAxisTemp = sumDisciplines(data, 21, "Civil Engineering")
        elif yAxisIn == "Comp":
            yAxisTemp = sumDisciplines(data, 27, "Computer Engineering")
        elif yAxisIn == "Elec":
            yAxisTemp = sumDisciplines(data, 33, "Electrical Engineering")
        elif yAxisIn == "EngPhys":
            yAxisTemp = sumDisciplines(data, 39, "Engineering Physics")
        elif yAxisIn == "Geo":
            yAxisTemp = sumDisciplines(data, 45, "Geological Engineering")
        elif yAxisIn == "Mining":
            yAxisTemp = sumDisciplines(data, 51, "Mining Engineering")
        
        mymatrix = consolidateEntries(xAxisTemp,yAxisTemp)
        
        #split mymatrix into 1d lists yAxis and xAxis
        yAxis = mymatrix[0]
        xAxis = mymatrix[1]
        
        #print out lists to test functionality
        print(yAxis)
        print(xAxis)
    #plots the respective sums of all disciplines in a pie or bar chart
    elif yAxisIn == "allDisciplines":
        xAxis = readTimeIn(data)
        yAxis = [["Applied Mathematics and Engineering","Chemical Engineering","Civil Engineering","Computer Engineering","Electrical Engineering","Engineering Physics","Geological Engineering","Mining Engineering"]]
        yAxisTemp = [0,0,0,0,0,0,0,0]
        unknownSum = 0
        for i in data[1:]:
            for j in range(0,8):
                sum = 0
                offset = 6*j
                for k in range(0,6):
                    index = k+9 + offset
                    if i[index]:
                        sum += int(i[index])
                yAxisTemp[j] += sum
        yAxis.append(yAxisTemp)
        print(yAxis)

    #plots a given topic of discussion vs time
    elif yAxisIn == "Academic Stress" or yAxisIn == "Academic Performance" or yAxisIn == "Academic Path" or yAxisIn == "Alcohol/substance abuse" or yAxisIn == "Disability" or yAxisIn == "Employment and/or Career Direction" or yAxisIn == "Extra-curricular involvement" or yAxisIn == "Financial Concerns" or yAxisIn == "Health and Fitness" or yAxisIn == "Time Management" or yAxisIn == "Organization" or yAxisIn == "Loneliness or Isolation" or yAxisIn == "Major life change/ Trauma" or yAxisIn == "Mental Health Issues" or yAxisIn == "Relationship with family or friend" or yAxisIn == "Relationship with partner" or yAxisIn == "Relationship with Professor/TA" or yAxisIn == "Sexual/Gender Identity" or yAxisIn == "Sexual Health" or yAxisIn == "Sleep" or yAxisIn == "Smoking" or yAxisIn == "Personal identity":
        xAxis = []
        xAxisTemp = readTimeIn(data)
        yAxis = []
        yAxisTemp = sumTopics(data,yAxisIn)
        mymatrix = consolidateEntries(xAxisTemp,yAxisTemp)
        #split mymatrix into 1d lists yAxis and xAxis
        yAxis = mymatrix[0]
        xAxis = mymatrix[1]

        #print out lists to test functionality
        print(yAxis)
        print(xAxis)



#sums the frequency of visit for the year to be graphed, for each data entry
def sumYears(data, startVal, label):
    #sets label
    yAxisTemp = [label]
    for j in data[1:]:
        sum = 0
        for k in range(0,8):
            index = startVal + 6*k
            if j[index]:
                sum += int(j[index])
        yAxisTemp.append(sum)
    return yAxisTemp

#iterates through xAxisTemp, searching for duplicate entries, and merging the sums of each yAxis of the respective index
def consolidateEntries(xAxisTemp,yAxisTemp):
    #init
    xAxis = []
    yAxis = []
    mymatrix = []
    yAxis.append(yAxisTemp[0])
    xAxis.append(xAxisTemp[0])
    counter = 1
    #iterate through xAxisTemp
    for l in xAxisTemp[1:]:
        #will catch any entries of xAxisTemp that have already been entered into xAxis
        if l in xAxis:
            existingNum = yAxis[xAxis.index(l)]
            yAxis[xAxis.index(l)] = existingNum + yAxisTemp[counter]
            counter += 1
        #will catch all unique entries
        else:
            xAxis.append(l)
            yAxis.append(yAxisTemp[xAxisTemp.index(l)])
            counter += 1

    #must append yAxis and xAxis into a matrix to return a sigle list
    mymatrix.append(yAxis)
    mymatrix.append(xAxis)
    return mymatrix

def sumDisciplines(data,startVal, label):
    #sets label
    yAxisTemp = [label]
    for j in data[1:]:
        sum = 0
        for k in range(0,6):
            index = k + startVal
            if j[index]:
                sum += int(j[index])
        yAxisTemp.append(sum)
    return yAxisTemp

def sumTopics(data, label):
    yAxisTemp = [label]
    for j in data[1:]:
        if label in j[4]:
            yAxisTemp.append(1)
        else:
            yAxisTemp.append(0)
    return yAxisTemp


#reads timestamps into temporary x-axis list, renames label appropriately
def readTimeIn(data):
    xAxisTemp = []
    for i in data:
        xAxisTemp.append(i[0][:9])
        xAxisTemp[0] = "Time"
    return xAxisTemp

#test call
'''makeGraphData("first","scatter")
    makeGraphData("second","scatter")
    makeGraphData("third","scatter")
    makeGraphData("fourth","scatter")
    makeGraphData("fifth","scatter")
    makeGraphData("allYears","scatter")'''
makeGraphData("Time Management","scatter")
