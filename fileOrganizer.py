import csv

#read in csv file to matrix 'data'
data = list(csv.reader(open('EWCForm_TestData.csv')))

#function that iterates through 'data' matrix and makes two new lists with pertinent information for graphing
def makeGraphData(yAxisIn, graphType):
    #plots a given year against time
    if yAxisIn == "first" or yAxisIn == "second" or yAxisIn == "third" or yAxisIn == "fourth" or yAxisIn == "fifth":
        #init
        xAxis = []
        xAxisTemp = []
        yAxis = []
        yAxisTemp = []
        #reads timestamps into temporary x-axis list, renames label appropriately
        for i in data:
            xAxisTemp.append(i[0])
        xAxisTemp[0] = "Time"
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
        yAxis = [["Fifth","Fourth","Third","Second","First","Unknown"]]
        yAxisTemp = [0,0,0,0,0,0]
        unknownSum = 0
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

#test call
'''makeGraphData("first","scatter")
    makeGraphData("second","scatter")
    makeGraphData("third","scatter")
    makeGraphData("fourth","scatter")
    makeGraphData("fifth","scatter")'''
makeGraphData("allYears","scatter")

