import csv

#reads data into matrix
data = list(csv.reader(open('EWCForm_TestData.csv')))

#Takes the comments from the CSV file and put them in a seperate matrix
def extractComments(n):
    #inti
    shiftComment = []
    oneOnOneConv = []
    whatWentWell = []
    suggestionsForNextMeeting = []
    comments = []

    #put each type of comment in a list
    for item in n:
        shiftComment.append(item[5])
    for item in n:
        oneOnOneConv.append(item[6])
    for item in n:
        whatWentWell.append(item[7])
    for item in n:
        suggestionsForNextMeeting.append(item[8])

    #make an array with each catagory of comment taking a different row
    comments.append(shiftComment)
    comments.append(oneOnOneConv)
    comments.append(whatWentWell)
    comments.append(suggestionsForNextMeeting)

    return comments

def mostRecentComment (n, comments):

    #init
    checker = True
    counter = 0
    entries = []
    lenColumn = len(n)
    firstEntry = lenColumn -1
    unformatedRecentComments = []
    recentComments = []
    catagory1 = []
    catagory2 = []
    catagory3 = []
    catagory4 = []



    mostRecentDate = n[firstEntry][0][:11] #takes only the date of the most recent log entry (year/month/day)

    while checker:
        i = firstEntry-counter

        if mostRecentDate == n[i][0][:11]:
            entries.append(i) #collects the indices of any other entries with the same dates

        #checks to see if the while loop is at the end of the matrix
        elif counter >= firstEntry:
            checker = False
        counter += 1
    #Collects the comments from the entries and organizes them into catagories
    for j in range(len(entries)):
        catagory1.append(n[entries[j]][5])
        catagory2.append(n[entries[j]][6])
        catagory3.append(n[entries[j]][7])
        catagory4.append(n[entries[j]][8])

    #Puts all of the entries into a single list so that they can be arranged by entry
    for k in range(len(catagory1)):
        unformatedRecentComments.append(catagory1[k])
        unformatedRecentComments.append(catagory2[k])
        unformatedRecentComments.append(catagory3[k])
        unformatedRecentComments.append(catagory4[k])

    #Arranges the data so each row is one entry of comments
    for l in range(len(entries)):
        indx1 = l*4
        indx2 = indx1 + 4
        recentComments.append(unformatedRecentComments[indx1:indx2])

    return recentComments


