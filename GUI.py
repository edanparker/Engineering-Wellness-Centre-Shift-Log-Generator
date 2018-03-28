from tkinter import *
import tkinter.messagebox
from datetime import datetime
import time

mainWindow = Tk() #window
canvas = Canvas(mainWindow, width = 500, height = 500)
myImage = PhotoImage(file = '/Users/charliemaslechko/PycharmProjects/MOD3/mainEWCFINAL.gif')
canvas.create_image(240, 295, anchor = NW, image = myImage)
canvas.pack()





passedStringOption = ""
passedStringGraphType = ""
dateOneArray = [0, 0, 0]
dateTwoArray = [0, 0, 0]




mainWindow.title("Engineering Wellness Center")
mainWindow.geometry("450x500")
mainWindow.configure(background = "white")

optionsX = ["Select an Option", "By Discipline", "By Year", "By Topic"]
graphType = ["Bar graph", "Histogram", "Pie chart", "Scatter plot"]
disciplinesAvailable = ["Mechanical", "Civil", "Chemistry", "Eng Phys", "Eng Chem", "Electrical", "Computer", "Geological", "Mining", "Apple"]
yearsAvailable = ["First", "Second", "Third", "Fourth", "Fifth", "Unknown"]


def passToFunction():


    def checkForCharacters():
        if (dateOneEntry[0:4].isdigit() == False or dateOneEntry[5:7].isdigit() == False or dateOneEntry[8:10].isdigit() == False):
            return True
        if (dateTwoEntry[0:4].isdigit() == False or dateTwoEntry[5:7].isdigit() == False or dateTwoEntry[8:10].isdigit() == False):
            return True

        return False



    errorCheck = False
    dateOneEntry = dateOne.get()
    dateTwoEntry = dateTwo.get()


    #initial error test for length
    if((len(dateOneEntry) != 10) or (len(dateTwoEntry) != 10)):
        errorCheck = True
    #check format for hyphen
    elif ((dateOneEntry[4] != '-') or (dateTwoEntry[4] != '-') or (dateOneEntry[7] != '-') or (dateTwoEntry[7] != '-')):
        errorCheck = True
    elif (checkForCharacters() == True):
        errorCheck = True

    #any of the catches above will be ended here for CPU usage
    #function breaks here if any of the above conditionals were met
    if (errorCheck == True):
        runErrorMessage()
        return


    #We have enough information that we know the values entered were numeric integers
    #convert text fields into arrays
    global dateOneArray
    global dateTwoArray
    dateOneArray = [int(dateOneEntry[0:4]), int(dateOneEntry[5:7]), int(dateOneEntry[8:10])]
    dateTwoArray = [int(dateTwoEntry[0:4]), int(dateTwoEntry[5:7]), int(dateTwoEntry[8:10])]


    #check to make sure the months are between 1 and 12
    if ((dateOneArray[1] < 1 or dateOneArray[1] > 12) or (dateTwoArray[1] < 1 or dateTwoArray[1] > 12)):
        errorCheck = True

    #months 1 3 5 7 8 10 12 all have 31 days
    if ((dateOneArray[1] == 1 or 3 or 5 or 7 or 8 or 10 or 12) or (dateTwoArray[1] == 1 or 3 or 5 or 7 or 8 or 10 or 12)):
        if ((dateOneArray[2] > 31 or dateOneArray[1] < 1) or (dateTwoArray[2] > 31 or dateTwoArray[2] < 1)):
            errorCheck = True

    #months 4 6 9 11 all have 31 days
    if ((dateOneArray[1] == 4 or 6 or 9 or 11) or (dateTwoArray[1] == 4 or 6 or 9 or 11)):
        if ((dateOneArray[2] > 30 or dateOneArray[1] < 1) or (dateTwoArray[2] > 311 or dateTwoArray[2] < 1)):
            errorCheck = True

    # any of the catches above will be ended here for CPU usage
    # UPDATE CATCH FOR CPU
    if (errorCheck == True):
        runErrorMessage()
    return



    #Everything should be caught by now to insert into python date object
    newdate1 = time.strptime(dateOneEntry, "%Y-%m-%d")
    newdate2 = time.strptime(dateTwoEntry, "%Y-%m-%d")


    #make sure dates are sequential and not the same
    if ((newdate1 > newdate2 == True) or (dateOneEntry == dateTwoEntry)):
        print("RUN")
        errorCheck = True




    #final error check
    if (errorCheck == True):
        runErrorMessage()
        return
    else:
        #*******RUN THE FUNCTION HERE***** insert global variables passedStringOption and passedStringGraphType and the arrays dateOneArray and dateTwoArray
        return




















def runErrorMessage():
    tkinter.messagebox.showinfo('Invalid Entry',
                                'Make sure to enter dates as follows:                    YYYY-MM-DD eg. 2017-04-27 describes April, 27, 2017')


def storeValueGraphType(option):
    global passedStringGraphType
    passedStringGraphType = option


def storeValueOption(option):
    print(option)
    global passedStringOption
    passedStringOption = option


def updateGraph(val):
    if (passedStringGraphType != "Pie chart"):
        if val == "By Discipline":
            showDisciplineOptions()
        else:
            disciplineOptionsLabel.place_forget()
            disciplineOptions.place_forget()
        if val == "By Year":
            showYearOptions()
        else:
            yearOptions.place_forget()
            yearOptionsLabel.place_forget()



def showDisciplineOptions():
    selectedOptionDiscipline = StringVar()
    selectedOptionDiscipline.set(disciplinesAvailable[0])
    disciplineOptions.place(x=0, y=200)
    disciplineOptionsLabel.place(x = 0, y = 180)

def showYearOptions():
    selectedYear = StringVar()
    selectedYear.set(yearsAvailable[0])
    yearOptions.place(x = 0, y = 200)
    yearOptionsLabel.place(x = 0, y = 180)


disciplineOptionsLabel = Label(mainWindow, text="Discipline Options:", font=("Courier", 15))
yearOptionsLabel = Label(mainWindow, text="Year Options:", font=("Courier", 15))
title = Label(mainWindow, text="Engineering Wellness Center", font=("Courier", 23))
graphOptionsLabelY = Label(mainWindow, text = "Y-Axis Options:", font=("Courier", 15))
timePeriod = Label(mainWindow, text = "Time Period:", font=("Courier", 15))
graphVisualOptionsLabel = Label(mainWindow, text = "Graph Type:", font=("Courier", 15))
toText = Label(mainWindow, text = "To", font=("Courier", 15))


#setting initial options

selectedOption = StringVar()
selectedOption.set(optionsX[0])

selectedOptionDiscipline = StringVar()
selectedOptionDiscipline.set(disciplinesAvailable[0])

selectedVisual = StringVar()
selectedVisual.set(graphType[0])

selectedYear = StringVar()
selectedYear.set(yearsAvailable[0])





#visual selection
graphVisualOptions = OptionMenu(mainWindow, selectedVisual, *graphType, command = storeValueGraphType)
#Primary selection
graphOptions = OptionMenu(mainWindow, selectedOption, *optionsX, command = updateGraph)
#sub options 1
disciplineOptions = OptionMenu(mainWindow, selectedOptionDiscipline, *disciplinesAvailable, command = storeValueOption)
yearOptions = OptionMenu(mainWindow, selectedYear, *yearsAvailable, command = storeValueOption)
#Date entry
dateOne = Entry(mainWindow)
dateTwo = Entry(mainWindow)

graphButton = Button(mainWindow, text = "Plot Graph", command = passToFunction)

dateOne.insert(END, 'YYYY-MM-DD')
dateTwo.insert(END, 'YYYY-MM-DD')

#titles
#main title
title.place(x=0,y=0)
#subtitles
timePeriod.place(x = 200, y = 40)
dateOne.place(x = 200, y = 60)
toText.place(x = 200, y = 89)
dateTwo.place(x = 200, y = 109)
graphOptions.place(x=0, y=130)
graphOptionsLabelY.place(x=0, y=110)

graphButton.place(x = 0, y = 245)
graphVisualOptions.place(x=0, y=60)
graphVisualOptionsLabel.place(x = 0, y = 40)




mainWindow.mainloop()












































