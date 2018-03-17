import matplotlib.pyplot as plt

'''
def selectGraph(timestampsList, yList, graphtype):
    if graphtype == "Scatter plot":
        #cut label
        #1 in time corresponds to 0 in y
        xList = timestampsList[1::]
        Scatter(xList, yList)

    if graphtype == "Histogram":
        Histogram(timestampsList)
    if graphtype == "Pie chart":
        
        Pie(freq, lab)
    if graphtype == "Bar graph":
        #stuff
'''


def Scatter(x_list, y_list):
    #works
    plt.scatter(x_list, y_list)
    plt.show()

def Pie(frequency_list, labels_list):
    #list of frequencies and list of labels if one of the frequencies is zero it and it's corresponding label must be removed before using this function
    #works
    plt.pie(frequency_list, explode=None, labels=labels_list)
    plt.show()

def Histogram(y_list):
    #works
    plt.hist(y_list)
    plt.show()

def BarChart(xVars_list, heights_list, labels_list):
    #works
    plt.bar(xVars_list, heights_list, tick_label=labels_list)
    plt.show()



#Test Scatter
'''
myXList = [1, 2, 3, 4, 5]
myYList = [6, 7, 8, 9, 10]

Scatter(myXList, myYList)
'''

#Test Pie
'''
myFrequencies = [1, 2, 0, 4, 5, 6]
myLabels = ["One", "Two", "Three", "Four", "Five", "Six"]

Pie(myFrequencies, myLabels)
'''

#Test Histogram
'''
my_X_Vals = [[3, 3, 3], [4, 4, 4, 4], [1], [2, 2]]
Histogram(my_X_Vals)
'''

#Test Bar
#'''
myxVars = [1, 3, 4, 5]
myHeights = [5, 1, 5, 3]
myLabels = ["One", "Two", "Three", "Four"]
BarChart(myxVars, myHeights, myLabels)
#'''