def GatherPatientData(fileName, processed):
    fileData = open(fileName, "r").read().splitlines()
    patientData = []

    if processed == False:
        tempPatient = []
        for line in fileData:
            for featureInfo in line.split():
                tempPatient.append(featureInfo)
                if len(tempPatient) == 76:
                    patientData.append(tempPatient)
                    tempPatient = []
    else:
        for line in fileData:
            patientData.append(line.split(","))

    return(patientData)

def FeatureInfermation(patientData, fileType):
    match(fileType):
        case 0:
            length = 76
        case 1:
            length = 14
        case _:
            print("Enter the number of features within your data")
            length = int(input("       : "))
    
    processedData = [[] for _ in range(length)]
    patientCount = 0
    for i in range(len(patientData)):

        for l in range(length):
            try:
                dataPoint = float(patientData[i][l])
            except:
                dataPoint = patientData[i][l]

            found = False
            for k in range(len(processedData[l])):
                if processedData[l][k][0] == dataPoint:
                    processedData[l][k][1] += 1
                    found = True
                    break

            if not found:
                processedData[l].append([dataPoint, 1])
        patientCount += 1
    DataOutput(processedData, patientCount)

def DataOutput(data, count):
    print("The feature information will be displayed in your chosen format, followed by the percentage of the data split relative to the overall data.")
    print("Enter 1: If you want to sort data by feature")
    print("Enter 2: If you want to sort data by population")
    choice = int(input("       : "))

    for i in range(len(data)):
        try:
            match(choice):
                case 1:
                    sortedData = sorted(data[i], key=lambda x: x[0])
                case _:
                    sortedData = sorted(data[i], key=lambda x: x[1])
        except:
            match(choice):
                case 1:
                    sortedData = sorted(data[i], key=lambda x: (x[0] == "?", x[0]))
                case _:
                    sortedData = sorted(data[i], key=lambda x: (x[1] == "?", x[1]))

        print("     Data for,", i+1," feature")

        for j in range(len(sortedData)):
            print(sortedData[j], round(sortedData[j][1]/count*100,2))

def GatherAllPatientData():
    totalFilesData = []
    chosen = False
    print("Enter the ID of the file you want to get data from:")
    print("Enter 0: When all wanted files have been chosen")
    print("The applcation will not work if unprocessed and processed files are used in tandom")
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
                fileData = GatherPatientData("cleveland - Copy.data", False)
                fileType = 0
            case 2:
                fileData = GatherPatientData("hungarian.data", False)
                fileType = 0
            case 3:
                fileData = GatherPatientData("long-beach-va.data", False)
                fileType = 0
            case 4:
                fileData = GatherPatientData("switzerland.data", False)
                fileType = 0
            case 5:
                fileData = GatherPatientData("processed.cleveland.data", True)
                fileType = 1
            case 6:
                fileData = GatherPatientData("processed.hungarian.data", True)
                fileType = 1
            case 7:
                fileData = GatherPatientData("processed.va.data", True)
                fileType = 1
            case 8:
                fileData = GatherPatientData("processed.switzerland.data", True)
                fileType = 1
            case 9:
                print("Enter the name of the file you would like to get data from")
                print("the file type will also need to be added (e.g: .csv, .data, ...)")
                fileName = input("       : ")
                fileData = GatherPatientData(fileName, True)#Code assumes that use files are in comma seperated and all patient data is on a single row
                fileType = 2
        totalFilesData += fileData
    return(totalFilesData, fileType)

def Menu():
    running = True 
    print("Welcome to Data Processing")
    print()
    print("To use the this code you will need to chose a function which you would like too use.")
    print("Then the code will ask whcih files you could like to use data from")
    print()
    while running == True:
        print("Enter 0: To stop the running of this applcation")
        print("Enter 1: To collect the feature quantative and population")
        print("Enter 2: To collect a chosen feature quantative and population")
        print("Enter 3: To collect feature quantative and population based off stage clasifiaction")
        print("Enter 4: To collect data breakdown (Average, Range, Distrabution)")
        print("Enter 5: To detect all missing or incorrct data")
        print("Enter 6: To process wanted data into a CSV file")
        choice = int(input("       : "))

        patientData, fileType = GatherAllPatientData()
        match(choice):
            case 1:
                FeatureInfermation(patientData, fileType)#done
            case 2:
                print("add code")
            case 3:
                print("add code")

    print("Thanks you for using this appcation")
    print("Have a greate day")
    
Menu()
