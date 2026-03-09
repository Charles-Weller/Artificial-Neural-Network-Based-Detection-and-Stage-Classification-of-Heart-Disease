def GatherPatientData(fileName, p):#p holds if the data is processed or not
    data = open(fileName, "r").read().splitlines()
    if p == 0:
        patientData = []
        tempPatient = []

        for line in data:
            for tok in line.split():
                tempPatient.append(tok)
                if len(tempPatient) == 76:
                    patientData.append(tempPatient)
                    tempPatient = []
    else:
        print("add code")

    print(patientData)
    return(patientData)


def ChoiceWantedFiles():
    totalFilesData = []
    chosen = False
    print("Enter the ID of the file you want to get data from:")
    print("Enter 0: When all wanted files have been chosen")
    print()
    print("Enter 1: for cleveland data")
    print("Enter 2: for hungarian data")
    print("Enter 3: for Long Beach data")
    print("Enter 4: for switzerland data")
    print("Enter 5: for processed cleveland data")
    print("Enter 6: for processed hungarian data")
    print("Enter 7: for processed long Beach data")
    print("Enter 8: for processed switzerland data")
    print("Enter 9: for a file of your choice")

    while chosen == False:
        choice = int(input("       : "))
        match(choice):
            case 0:
                break
            case 1:
                fileData = GatherPatientData("cleveland - Copy.data", 0)
            case 2:
                fileData = GatherPatientData("hungarian.data", 0)
            case 3:
                fileData = GatherPatientData("long-beach-va.data", 0)
            case 4:
                fileData = GatherPatientData("switzerland.data", 0)
            case 5:
                fileData = GatherPatientData("processed.cleveland.data", 1)
            case 6:
                fileData = GatherPatientData("processed.hungarian.data", 1)
            case 7:
                fileData = GatherPatientData("processed.va.data", 1)
            case 8:
                fileData = GatherPatientData("processed.switzerland.data", 1)
            case 9:
                print("Enter the name of the file you would like to get data from")
                print("the file type will also need to be added (e.g: .csv, .data, ...)")
                fileName = input("       : ")
                fileData = GatherPatientData(fileName, 1)#Code assumes that use files are in comma seperated and all patient data is on a single row
        totalFilesData += fileData
        print("hi")

def Menu():
    running = True 
    print("Welcome to Data Processing")
    print()
    print("To use the this code you will need to chose a function which you would like too use.")
    print("Then the code will ask whcih files you could like to use data from")
    print()
    while running == True:
        print("Enter  1: To collect the feature options and population")
        print()
        print("Enter  0: To stop the running of this applcation")
        choice = int(input("       : "))

        patientData = ChoiceWantedFiles()
        match(choice):
            case 1:
                print("add code")

    print("Thanks you for using this appcation")
    print("Have a greate day")


    print("Enter 4:  To collect data on a peticular feture from all unprocessed file")
    print("Enter 5:  To collect data on a peticular feature from all processed file")
    print("Enter 6:  To collect data on a peticular feature from one file")
    print("Enter 7:  To collect all data from one file based off patient output")## Add options such as for a indevdule featrure 
    print("Enter 8:  To detect all missing or incorrect data from all unprocessed files")
    print("Enter 9:  To detect all missing and incorrect data from all processed files")
    print("Enter 10: To collect all missing and incorrect data from one file")
    print("Enter 11: To process wanted data into a CVS file")
    print("ENter 12: To collect the ranges for for each each sction of data based of outputs ")##
    print("Enter 13: To collect the ranges for each feature from selected code")
    print("Enter 14: To collect the average from each section of data based of outputs")
    print("Enter 15: To collect the average from each section of data based of outputs ")


Menu()
