import numpy as np
import pandas as pd

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

def FeatureInfermation(patientData, fileType, function):
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
    if function == 0:
        DataOutput(processedData, patientCount, None)
    else:
        return processedData, patientCount

def FeatureInfermationDeseaseClassifiaction(patientData, fileType, function):
    match(fileType):
        case 0:
            length = 76
            classificationPosition = 57
        case 1:
            length = 14
            classificationPosition = 13
        case _:
            print("Enter the number of features within your data")
            length = int(input("       : "))

            print("Enter the feature ID for the classification of the patient")
            classificationPosition = int(input("       : ")) - 1
    
    processedData = [[[] for _ in range(length)] for _ in range(5)]
    patientCount = 0
    for i in range(len(patientData)):

        if patientData[i][classificationPosition] == "0":
            n = 0
        elif patientData[i][classificationPosition] == "1":
            n = 1
        elif patientData[i][classificationPosition] == "2":
            n = 2
        elif patientData[i][classificationPosition] == "3":
            n = 3
        else:
            n = 4

        for l in range(length):
            try:
                dataPoint = float(patientData[i][l])
            except:
                dataPoint = patientData[i][l]

            found = False
            for k in range(len(processedData[n][l])):
                if processedData[n][l][k][0] == dataPoint:
                    processedData[n][l][k][1] += 1
                    found = True
                    break

            if not found:
                processedData[n][l].append([dataPoint, 1])
        patientCount += 1
    if function == 0:
        for i in range(5):
            DataOutput(processedData[i], patientCount, i)
    else:
        return processedData, patientCount

def MissingData(patientData, fileType, function):
    totalData, patientCount = FeatureInfermation(patientData, fileType, 1)
    numberOfFeatures = len(totalData)
    updatedData = [[] for _ in range(numberOfFeatures)]
    errorData = [[] for _ in range(numberOfFeatures)]

    if numberOfFeatures == 76:
        NON = [8,9,11,19,20,21,27,28,30,31,32,33,34,35,36,41,42,44,45,50,54,55,56,59,60,61,62,63,64,65,66,67,73]
    elif numberOfFeatures == 14:
        NON = [2,3,4]#Non zero Numbers
    else:
        enter =  False
        NON = []
        print("Enter the feature number where the it is not posible for the value to be 0")
        print("Enter 0 : When you are enteded all feature id's needed")
        print("Enter -1: To see the enteded features")
        while enter == False:
            featureChoice = int(input("       : "))

            if featureChoice == -1:
                NON = sorted(set(NON))
                print(NON)
            elif featureChoice == 0:
                enter = True
            else:
                NON.append(featureChoice)

    for i in range(numberOfFeatures):
        for j in range(len(totalData[i])):
            if i in NON and totalData[i][j][0] == 0.0:
                errorData[i].append(totalData[i][j])
            elif totalData[i][j][0] == -9.0 or totalData[i][j][0] == "?":
                errorData[i].append(totalData[i][j])
            else:
                updatedData[i].append(totalData[i][j])
    if function == 0:
        DataOutput(errorData, patientCount, None)
    else:
        return updatedData, patientCount

def FeatureStatistics(data, fileType, function):
    classifiedData, _ = FeatureInfermationDeseaseClassifiaction(data, fileType, 1)

    if function == 0:
        print("Enter the feature number you would like to collect the data on")
        print("Enter 0 if you would like to recive all feature data")
        featureChoice = int(input("       : "))
        print()

        print("Enter graph type:")
        print("Enter 0: To not display any graph")
        print("Enter 1: To display a Scatter graph")
        print("Enter 2: To display a Histogram")
        print("Enter 3: To display a Box plot")
        print("Enter 4: To display a Bar chart (average per classification)")
        print("Enter 5: To display a Heatmap")
        showGraph = int(input("       : "))
        print()
    else:
        featureChoice = function
        showGraph = 0

    if featureChoice == 0 or function != 0:
        length = len(classifiedData[0])
    else:
        length = 1

    FunctionAverages = [[0 for _ in range(length)] for _ in range(5)]

    for i in range(length):
        if length == 1:
            i = featureChoice - 1

        if function == 0:
            print("     Data for, feature", i + 1)
            print("Classification statistics:")

        xValues = []
        yValues = []
        groupedValues = []
        barAverages = []

        for j in range(5):
            classNumericValues = []

            for l in range(len(classifiedData[j][i])):
                try:
                    value = float(classifiedData[j][i][l][0])
                    count = classifiedData[j][i][l][1]

                    for _ in range(count):
                        classNumericValues.append(value)
                        xValues.append(j)
                        yValues.append(value)
                except:
                    pass

            groupedValues.append(classNumericValues)

            if len(classNumericValues) == 0:
                if function == 0:
                    print("Classification", j, ": No valid numeric data")
                    print()
                barAverages.append(0)
            else:
                classAverage = np.mean(classNumericValues)
                FunctionAverages[j][i] = classAverage
                classMinimum = min(classNumericValues)
                classMaximum = max(classNumericValues)

                if function == 0:
                    print("Classification", j)
                    print("Average:", round(classAverage, 4))
                    print("Standard Deviation:", round(np.std(classNumericValues), 4))
                    print("Variance:", round(np.var(classNumericValues), 4))
                    print("Min:", classMinimum)
                    print("Max:", classMaximum)
                    print("Range:", classMaximum - classMinimum)
                    print("Valid data points:", len(classNumericValues))
                    print()

                barAverages.append(classAverage)

        if showGraph != 0:

            if len(yValues) == 0:
                print("No valid numeric data available to plot for feature", i + 1)
                print()
            else:
                import matplotlib.pyplot as plt
                if showGraph == 1:
                    plt.scatter(xValues, yValues)
                    plt.title("Feature " + str(i + 1) + " by Classification")
                    plt.xlabel("Classification")
                    plt.ylabel("Feature Value")
                    plt.xticks([0,1,2,3,4])

                elif showGraph == 2:
                    plt.hist(yValues, bins=10)
                    plt.title("Histogram for Feature " + str(i + 1))
                    plt.xlabel("Feature Value")
                    plt.ylabel("Frequency")

                elif showGraph == 3:
                    plt.boxplot(groupedValues, tick_labels=[0,1,2,3,4])
                    plt.title("Box Plot for Feature " + str(i + 1) + " by Classification")
                    plt.xlabel("Classification")
                    plt.ylabel("Feature Value")

                elif showGraph == 4:
                    plt.bar([0,1,2,3,4], barAverages)
                    plt.title("Average Feature " + str(i + 1) + " by Classification")
                    plt.xlabel("Classification")
                    plt.ylabel("Average Value")

                elif showGraph == 5:

                    heatData = []

                    for group in groupedValues:
                        if len(group) == 0:
                            heatData.append([0]*40)
                        else:
                            hist, _ = np.histogram(group, bins=40)
                            heatData.append(hist)

                    heatData = np.array(heatData)

                    plt.figure(figsize=(12,6))

                    plt.imshow(heatData, aspect='auto', cmap='inferno', interpolation='bicubic')
                    plt.colorbar(label="Frequency")
                    plt.title("Heatmap of Feature " + str(i + 1))
                    plt.xlabel("Feature Value Bins")
                    plt.ylabel("Classification")
                    plt.yticks([0,1,2,3,4])

                    plt.show()

                else:
                    print("Invalid graph option selected.")
                    plt.close()
                    continue

                plt.show()

    if function != 0:
        return FunctionAverages

    print()

def PatientDataUpdate(patientData, fileType):
    match(fileType):
        case 0:
            length = 76
            classificationPosition = 57
            NON = [8,9,11,19,20,21,27,28,30,31,32,33,34,35,36,41,42,44,45,50,54,55,56,59,60,61,62,63,64,65,66,67,73]
        case 1:
            length = 14
            classificationPosition = 14
            NON = [2,3,4]
        case _:
            print("Enter the number of features within your data")
            length = int(input("       : "))

            print("Enter the feature ID for the classification of the patient")
            classificationPosition = int(input("       : ")) - 1

            enter =  False
            NON = []
            print("Enter the feature number where the it is not posible for the value to be 0")
            print("Enter 0 : When you are enteded all feature id's needed")
            print("Enter -1: To see the enteded features")
            while enter == False:
                featureChoice = int(input("       : "))

                if featureChoice == -1:
                    NON = sorted(set(NON))
                    print(NON)
                elif featureChoice == 0:
                    enter = True
                else:
                    NON.append(featureChoice)

    FunctionAverages = FeatureStatistics(patientData, fileType, 1)
    for i in range(len(patientData)):
        for j in range(length):
            if j in NON and (patientData[i][j] == "0.0" or patientData[i][j] == "0"):
                patientData[i][j] = FunctionAverages[int(patientData[i][classificationPosition])][j]
            elif patientData[i][j] == "-9.0" or patientData[i][j] == "-9" or patientData[i][j] == "?":
                 patientData[i][j] = FunctionAverages[int(patientData[i][classificationPosition])][j]
    return patientData

def Normalisation(x: np.ndarray):# Min Max 
    x = np.asarray(x, dtype=np.float64)

    minimum  = np.min(x)
    differance = np.max(x) - minimum

    if np.isclose(differance, 0.0):
        return np.zeros_like(x, dtype=np.float64)
    
    return (x - minimum ) / differance

def SaveNewData(patientData, fileType):
    print("Enter 1: To replaces missing or incorrect data with the clasifiction average")
    correctionchoice = int(input("       : "))
    if correctionchoice == 1:
        patientData = PatientDataUpdate(patientData, fileType)

    enter =  False
    wantedFeature = []
    print("Enter the feature number you would like to remove")
    print("Enter 0 : When you are enteded all feature id's wanted")
    print("Enter -1: To see the enteded features")
    while enter == False:
        featureChoice = int(input("       : "))

        if featureChoice == -1:
            wantedFeature = sorted(set(wantedFeature))
            print(wantedFeature)
        elif featureChoice == 0:
            enter = True
        else:
            wantedFeature.append(featureChoice)

    wantedFeature = sorted(set(wantedFeature), reverse=True)

    for i in range(len(patientData)):
        for j in range(len(wantedFeature)):
            del patientData[i][wantedFeature[j]-1]
    print()
    print("Enter 1 if you would like to normalise your dataset, Otherwise enter 0")
    normChoice = int(input("       : "))
    try:
        if normChoice == 1:  
            data = np.asarray(patientData, dtype=np.float64)
            for j in range(data.shape[1]):
                data[:, j] = Normalisation(data[:, j])

                patientData = data.tolist()
    except:
        print()
        print("Normalisation failed due to the presence of non-numeric data")
    print()

    if fileType == 0:
        columnNames = ["id", "ccf", "age", "sex", "painloc", "painexer", "relrest", "pncaden", "cp", "tresrbps", "htn", "chol", "smoke", "cigs", "years","fbs", 
                       "dm", "famhist", "restecg", "ekgmo", "ekgday", "ekgyr", "dig", "prog", "nitr", "pro", "diuretic", "proto", "thaldur", "thaltime", "met", 
                       "thalach", "thalrest", "tpeakbps", "tpeakbpd", "dummy", "trestbpd", "exang", "xhypo", "oldpeak", "slope", "rldv5", "rldv5e", "ca", "restckm", 
                       "exerckm", "restef", "restwm", "exeref", "exerwm", "thal", "thalsev", "thalpul", "earlobe", "cmo", "cday", "cyr", "num", "lmt", "ladprox", 
                       "laddist", "diag", "cxmain", "ramus", "om1", "om2", "rcaprox", "rcadist", "lvx1", "lvx2", "lvx3", "lvx4", "lvf", "cathef", "junk", "name"]
    elif fileType == 1:
        columnNames = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","num"]
    else:
        enter =  False
        columnNames = []
        print("Enter the feature headers (header need to be ended in order)")
        print("Enter 0 : When you are enteded all feature id's wanted")
        print("Enter -1: To see the enteded features")
        while enter == False:
            featureChoice = input("       : ")

            if featureChoice == "-1":
                print(columnNames)
            elif featureChoice == "0":
                enter = True
            else:
                columnNames.append(featureChoice)
    
    print("Enter the name which you would like to file to be called")
    choicenFileName = input("       : ")

    wantedFeature = sorted(set(wantedFeature), reverse=True)

    for l in range(len(wantedFeature)):
        del columnNames[wantedFeature[l]-1]
    df = pd.DataFrame(patientData, columns=columnNames)
    df.to_csv(choicenFileName+".csv", index=False)
    print()
    print("CSV saved successfully.")
    print()


def DataOutput(data, count, classification):
    print("The feature information will be displayed in your chosen format, followed by the percentage of the data split relative to the overall data.")
    print("Enter 1: If you want to sort data by feature")
    print("Enter 2: If you want to sort data by population")
    choice = int(input("       : "))
    print()
    print("Enter the feature number you would like to collect the data on")
    print("Enter 0 if you would like to recive all feature data")
    featureChoice = int(input(("       : ")))
    
    if featureChoice == 0:
        length = len(data)
    else:
        length = 1

    for i in range(length):
        try:
            if choice == 1:
                sortedData = sorted(data[featureChoice-1] if length == 1 else data[i],key=lambda x: x[0])
            else:
                sortedData = sorted(data[featureChoice-1] if length == 1 else data[i],key=lambda x: x[1])
        except:
            match(choice):
                case 1:
                    sortedData = sorted(data[featureChoice-1] if length == 1 else data[i],key=lambda x: (x[0] == "?", x[0]))
                case _:
                    sortedData = sorted(data[featureChoice-1] if length == 1 else data[i],key=lambda x: (x[1] == "?", x[1]))

        print("     Data for,", i+1, "feature", ("Classification " + str(classification)) if classification is not None else "")
        if sortedData == []:
            print("There is no missing or incorrect data")
        else:
            for j in range(len(sortedData)):
                print(sortedData[j], (round(sortedData[j][1]/count*100,2),"%"))
    print()

def GatherAllPatientData():
    totalFilesData = []
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

    while True:
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
                fileData = GatherPatientData(fileName, True)#Code assumes that use files are in comma seperated format and all patient data is on a single row
                if fileName.lower().endswith(".csv"):
                    fileData = fileData[1:]
                fileType = 2
        totalFilesData += fileData
    return(totalFilesData, fileType)

def Menu():
    running = True 
    print("Welcome to Data Processing")
    print()
    print("To use the this code you will need to chose a function which you would like too use.")
    print("Then the code will ask whcih files you could like to use data from")
    print("Once you reach the output stage there will be an option to recive data for all features or a select feature")
    print()
    while running == True:
        print("Enter 0: To stop the running of this applcation")
        print("Enter 1: To collect the feature quantative and population")
        print("Enter 2: To collect feature quantative and population based off stage clasifiaction")
        print("Enter 3: To collect data breakdown (Average, Range, Distrabution)")
        print("Enter 4: To detect all missing or incorrct data")
        print("Enter 5: To process wanted data into a CSV file")
        choice = int(input("       : "))
        print()
        if choice != 0:
            patientData, fileType = GatherAllPatientData()
        print()
        match(choice):
            case 0:
                break 
            case 1:
                FeatureInfermation(patientData, fileType, 0)
            case 2:
                FeatureInfermationDeseaseClassifiaction(patientData, fileType, 0)
            case 3:
                FeatureStatistics(patientData, fileType, 0)
            case 4:
                MissingData(patientData, fileType, 0)
            case 5:
                SaveNewData(patientData, fileType)

    print("Thanks you for using this appcation")
    print("Have a greate day")

Menu()
