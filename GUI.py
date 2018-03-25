from tkinter import *
import tkinter.messagebox

mainWindow = Tk() #window
canvas = Canvas(mainWindow, width = 500, height = 500)
myImage = PhotoImage(file = '/Users/charliemaslechko/PycharmProjects/MOD3/mainEWCFINAL.gif')
canvas.create_image(240, 295, anchor = NW, image = myImage)
canvas.pack()



passedStringOption = ""
passedStringGraphType = ""



mainWindow.title("Engineering Wellness Center")
mainWindow.geometry("450x500")
mainWindow.configure(background = "white")

optionsX = ["Select an Option", "By Discipline", "By Year"]
graphType = ["Bar graph", "Histogram", "Pie chart", "Scatter plot"]
disciplinesAvailable = ["Mechanical", "Civil", "Chemistry", "Eng Phys", "Eng Chem", "Electrical", "Computer", "Geological", "Mining", "Apple"]
yearsAvailable = ["First", "Second", "Third", "Fourth", "Fifth", "Unknown"]


def passToFunction():
    dateOneEntry = dateOne.get()
    dateTwoEntry = dateTwo.get()

    #initial error test for length

    #check format for hyphen


    if((len(dateOneEntry) != 10) or (len(dateTwoEntry) != 10)):
        runErrorMessage()

    if((dateOneEntry[4] or dateTwoEntry[4]  != '-') or (dateOneEntry[7] or dateTwoEntry[7] != '-')):
        runErrorMessage()




    #date input will be seperated into 2 arrays

    dateOneArray = [dateOneEntry[0:4], dateOneEntry[5:7], dateOneEntry[8:10]]
    #looking at the first text field


    #only run edans function





def runErrorMessage():
    tkinter.messagebox.showinfo('Invalid Entry',
                                'Make sure to enter dates as follows:                    YYYY-MM-DD eg. 2017-04-27 describes April, 27, 2017')


def storeValueGraphType(option):
    print(option)
    passedStringGraphType = option




def storeValueOption(option):
    print(option)
    passedStringOption = option


def updateGraph(val):
    print(val)
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
graphOptions.place(x=0, y=130)
graphOptionsLabelY.place(x = 0, y = 110)
timePeriod.place(x = 200, y = 40)
dateOne.place(x = 200, y = 60)
toText.place(x = 200, y = 89)
dateTwo.place(x = 200, y = 109)

graphButton.place(x = 0, y = 245)
graphVisualOptions.place(x=0, y=60)
graphVisualOptionsLabel.place(x = 0, y = 40)




mainWindow.mainloop()

