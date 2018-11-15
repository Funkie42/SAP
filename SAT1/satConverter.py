import readFile
import writeFile
import interface
import math
import random
import copy

counter = 0
colNumber = 0
lineNumber = 0

# convert the array syntax to an ascending number sequence
def writeNumbersInFormat(line, colmun, colNumber):
    numberToBeAdded = str(line * colNumber + colmun +1)
    return numberToBeAdded


def addSantaClauses(line, column, colNumber, lineNumber):
    hoehoehoe = []

    # Check Horizontal 3 in a row
    # "left left middle" and  "middle right right" are not neccessary because they are redundant
    # we only check "left middle right"

    if (column > 0) & (column < colNumber - 1):
        for i in range(2):
            hoehoehoe.append([writeNumbersInFormat(line, column - 1, colNumber),
                              writeNumbersInFormat(line, column, colNumber),
                              writeNumbersInFormat(line, column + 1, colNumber)])
            # make content negative
            if i == 1:
                for j in range(3):
                    hoehoehoe[len(hoehoehoe) - 1][j] = "-" + hoehoehoe[len(hoehoehoe) - 1][j]
        '''for i in range(6):
            hoehoehoe.append([writeNumbersInFormat(line, column - 1, colNumber),
                            writeNumbersInFormat(line, column, colNumber),
                            writeNumbersInFormat(line, column + 1, colNumber)])
            if i > 2:
                for j in range(2):
                    hoehoehoe[len(hoehoehoe) - 1][((i-3)+j)%3] = "-" + hoehoehoe[len(hoehoehoe) - 1][((i-3)+j)%3]
            else:
                hoehoehoe[len(hoehoehoe) - 1][i] = "-" + hoehoehoe[len(hoehoehoe) - 1][i]'''

    # Check vertical 3 in a row
    if (line > 0) & (line < lineNumber - 1):
        for i in range(2):
            hoehoehoe.append([writeNumbersInFormat(line - 1, column, colNumber),
                              writeNumbersInFormat(line, column, colNumber),
                              writeNumbersInFormat(line + 1, column, colNumber)])
            if i == 1:
                for j in range(3):
                    hoehoehoe[len(hoehoehoe) - 1][j] = "-" + hoehoehoe[len(hoehoehoe) - 1][j]
    return hoehoehoe

# Check Lines for 50/50 distribution
# Check Columns for 50/50 distribution
def addAmountDistriction(lineNumber, colNumber, vertical, data):
    sack = []
    solutions = []
    for i in range(lineNumber):
        arrayOfCurrentRowIndexes = []
        for j in range(colNumber):
            if vertical:
                #print (data,"data")
                #print (lineNumber,"lineNum")
                arrayOfCurrentRowIndexes.append(data[i * lineNumber + j])
            else:
                arrayOfCurrentRowIndexes.append(data[j * lineNumber + i])
        whiteBlocks = []
        blackBlocks = []
        for elem in arrayOfCurrentRowIndexes:
            if elem > 0:
                whiteBlocks.append(elem)
            elif elem < 0:
                blackBlocks.append(elem)

        surplusOfWhiteBlocks = len(whiteBlocks) - len(arrayOfCurrentRowIndexes)//2

        if surplusOfWhiteBlocks < 0:
            sack = [[]]
            for i in blackBlocks:
                sack[0].append(i*-1)
            return sack
            solutions = buildAllPossibleNegationsIterative(surplusOfWhiteBlocks*-1, len(blackBlocks), blackBlocks, 1)
        elif surplusOfWhiteBlocks > 0:
            sack = [[]]
            for i in whiteBlocks:
                sack[0].append(i*-1)
            return sack

        #The main algorithm is called
        #solutions = buildAllPossibleNegationsIterative(colNumber//2-1, colNumber, arrayOfCurrentRowIndexes)
        for s in solutions:
            sack.append(s)
    return (sack)

def buildAllPossibleNegationsIterative(negationAmount, varAmount, arrayOfLineData, reverse):
    cnfOfLineCheckArray = []

    for negLevel in range(0, negationAmount+1):

        positionToWrite = negLevel
        startPosWrite = negLevel

        numbersToNeg = []
        for i in range(negLevel):
            numbersToNeg.append(i+1)

        #Main loop to write each possibility
        calculating = 1
        while calculating:


            newCNF = arrayOfLineData.copy()


            #LENGTH of array to flip numbers
            for number in numbersToNeg:

                newCNF[number-1] *= -1

            if len(numbersToNeg) > 0:
                for number in range(0, len(numbersToNeg)):
                    if (numbersToNeg[number] == varAmount-(len(numbersToNeg)-number-1)):
                        if number==0:
                            calculating = 0  # End Program because it's finished for NegAmount
                        else:
                            numbersToNeg[number-1] += 1
                            numbersToNeg[number] = numbersToNeg[number-1]

                if numbersToNeg[len(numbersToNeg) - 1] < varAmount:
                    numbersToNeg[len(numbersToNeg) - 1] += 1
            else:
                calculating = 0

            cnfOfLineCheckArray.append(newCNF)

    for j in range(len(cnfOfLineCheckArray[0])):
       cnfOfLineCheckArray[0][j] = cnfOfLineCheckArray[0][j] * -1

    return cnfOfLineCheckArray

#RECURSIVE! VERY INEFFICENT!
#returns all pos and negativ possibility for a given amout of negations and variables
def buildAllPossibleNegationsRecursive(negationAmout, varAmount, arrayOfLineData, changedNumbers = []):
    solutions = []
    if negationAmout == 0:

        arrayOfLineData = arrayOfLineData + changedNumbers
        arrayOfLineDataNeg = []
        for i in arrayOfLineData:
            dataNegative = i*-1
            arrayOfLineDataNeg.append(dataNegative)
        solutions.append(arrayOfLineDataNeg)
        solutions.append(arrayOfLineData)

        return solutions


    for i in range(varAmount):
        modArray = arrayOfLineData.copy()
        changedNumbers.append(-modArray.pop(i))

        solution = buildAllPossibleNegationsRecursive(negationAmout-1, varAmount-1, modArray, changedNumbers)

        del changedNumbers[-1]
        solutions.extend(solution)
    return solutions


def convertToSat(data, repeatNumber = 0):
    # Read input data to Array "data"
    global colNumber, lineNumber
    writemode = ""

    cnf = []

    #3 Blocks Rule applied
    if repeatNumber == 0:
        colNumber = len(data[0])
        lineNumber = len(data)
        for i in range(lineNumber):
            for j in range(colNumber):

                '''Insert given blockcolors as Unit-Clauses
    
                White blocks are represented by a positive value
                Black blocks are represented by a negative value
                '''
                if data[i][j] == 1:  # Insert white blocks
                    cnf.append([writeNumbersInFormat(i, j, colNumber)])

                elif data[i][j] == 2:  # Insert black blocks
                    cnf.append(["-" + writeNumbersInFormat(i, j, colNumber)])

                # Check only unknown blocks (Grey blocks)

                # check all stones and append logic on them add clauses to determine unknown blocks
                santasHoeCollection = addSantaClauses(i, j, colNumber, lineNumber)
                for clause in santasHoeCollection:
                    cnf.append(clause)
        writemode = "w+"

    #Row Col Restiction appended
    else:

        lineRestictions = addAmountDistriction(lineNumber, colNumber, 1, data)
        for lineRestiction in lineRestictions:
            cnf.append(lineRestiction)

        colRestictions = addAmountDistriction(colNumber, lineNumber, 0, data)
        for colRestiction in colRestictions:
            cnf.append(colRestiction)
        writemode = "a"

    # number of literals and terms
    lits = colNumber * lineNumber
    terms = len(cnf)

    # write converted CNF to File
    writeFile.writeCNF(lits, terms, cnf, writemode)

# checks if equal amout of white and black in every row
def checkIfDataIsDevineLines(data, cols, lines):
    for i in range(lines):
        counter = 0
        for j in range(cols):
            if(data[i * lineNumber + j] > 0):
                counter = counter + 1
        if(counter != colNumber//2):
            return 0
    return 1

def checkIfDataIsDevineCols(data, cols, lines):
    for i in range(lines):
        counter = 0
        for j in range(cols):
            #print("line: ", i, "col: ", j, "data: ", data[i + lines * j])
            if(data[i+lines*j] > 0):

                counter = counter + 1
        #print("counter: ", counter, "lineNumber: ", lineNumber)
        if(counter != lineNumber//2):

            return 0
    return 1

def convertData(data, lines, cols):
    sol = []
    counter = 0
    for i in range(lines):
        subSol = []
        for j in range(cols):
            if (data[counter] < 0):
                subSol.append(2)
            else:
                subSol.append(1)
            counter += 1
        sol.append(subSol)
    return sol

def applyRules(data, lines, cols, greyFields, buildingBoard = 0):
    # apply the rule for the 3 solver
    convertToSat(data)
    data = readFile.readPicosatSolution(cols, lines, 0)
    # call the code to add clauses for amount restriction
    convertToSat(data, 1)
    data = readFile.readPicosatSolution(cols, lines, 0)
    puzzleSolved = 0
    i = 0
    while (puzzleSolved == 0):
        convertToSat(data, 1)
        data = readFile.readPicosatSolution(cols, lines, 0)
        # check if equal amount in al rows
        puzzleSolved = checkIfDataIsDevineLines(data, cols, lines)
        if (puzzleSolved == 1):
            # check if all rows are equal
            puzzleSolved = checkIfDataIsDevineCols(data, cols, lines)
            # satConverter.convertToSat(data, 1)
            data = readFile.readPicosatSolution(cols, lines, 0)

        i = i + 1
    # we have found the perfect solution but now exclude all other possibilities
    # herefor we got throug everystone and check if it could be switched
    # if so we have to write this stone in our satfile
    if not buildingBoard:
        checkEveryStoneForOtherSolutions(data, greyFields)


    # data = readFile.readPicosatSolution(cols, lines, 1)
    data = convertData(data, lines, cols)
    return data

''''# gets data in fomat: [1,2,3,4,5,6,7,8,9,...,n]
def checkEveryStoneForOtherSolutions(data):
    gameData = readFile.readFileData('./ueb1/u01puzzle-small1.txt')

    lits = colNumber * lineNumber
    for elem in data:
        #check it for the negative value if it would be possible in other solution
        elem = elem*-1
        isPossible = readFile.readPicosatWithArgs(str(elem))
        if(isPossible==1):
            elem = elem*-1
            #it can be switched and therefor this possibility has to be excluded
            writeFile.writeCNF(lits, 1, [[elem]], "a")'''

# gets data in fomat: [1,2,3,4,5,6,7,8,9,...,n]
def checkEveryStoneForOtherSolutions(data, greyFields, isBuildingNewBoard = 0):

    lits = colNumber * lineNumber
    counter = 0
    for elem in greyFields:
        counter += 1
        #check it for the negative value if it would be possible in other solution
        elem = data[elem]*-1
        isPossible = readFile.readPicosatWithArgs(str(elem))
        if isPossible == 1:
            if isBuildingNewBoard:
                return 0 #Not unique anymore! Boardbuilding
            else:
                elem = elem*-1
                #it can be switched and therefor this possibility has to be excluded
                writeFile.writeCNF(lits, 1, [[elem]], "a")
    return 1 #Still unique board

#Aufgabe 4
def buildNewGrid(lines, cols):
    gameField = []
    greyFields = []
    gridSize = lines*cols
    for i in range(gridSize):
        gameField.append(0)
    for i in range(gridSize//10):
        index = random.randint(0,gridSize-1)
        gameField[index] = random.randint(1,2)
    counter = 0
    for i in range(len(gameField)):
        if(gameField[i] == 0):
            greyFields.append(counter)
        counter += 1

    arrayInFormat = []
    newArrayToAdd = []
    for i in range(len(gameField)):

        newArrayToAdd.append(gameField[i])

        if i % lines == lines - 1:
            arrayInFormat.append(newArrayToAdd)
            newArrayToAdd = []

    return setFieldsForSingularity(arrayInFormat,greyFields, lines, cols)

def setFieldsForSingularity(arrayInFormat, greyFields, lines, cols):
    lits = lines * cols
    data = applyRules(arrayInFormat, lines, cols, greyFields)
    applyRules(data, lines, cols, greyFields)

    #just do it through deleting elements

    #until at least half the field is empty
    oldSolution = copy.deepcopy(data)
    greyFields = greyFields
    oldGreyFields = copy.deepcopy(greyFields)
    counter = 0
    successfulReduction = 0
    while (counter < len(data)) | (successfulReduction*lines < len(data)//2):

        counter += 1
        for line in range(len(data)):
            newLinegreyFields = []
            indizeToDelete = random.randint(0, len(data[line])-1)
            if indizeToDelete+line*lines in greyFields:
                del greyFields[greyFields.index(indizeToDelete+line*lines)]

                data[line][indizeToDelete] = 0
                newLinegreyFields.append(indizeToDelete+line*lines)

            dataInOtherFormat = []
            for j in oldSolution:
                for k in j:
                    dataInOtherFormat.append(k)
            applyRules(data, lines, cols, greyFields)
            unique = checkEveryStoneForOtherSolutions(dataInOtherFormat, newLinegreyFields, 1)

            if unique == 0:
                data = copy.deepcopy(oldSolution)
                greyFields = copy.deepcopy(oldGreyFields)
                unique == 1
            else:
                oldSolution = copy.deepcopy(data)
                oldGreyFields = copy.deepcopy(greyFields)
                successfulReduction += 1

    #old, wrong solution
    '''counter = 0
    for elem in greyFields:
        # check it for the negative value if it would be possible in other solution
        #print ("data",data)
        #elemNegated = (data[elem//lineNumber][elem%colNumber]) % 2 + 1
        #if elemNegated == 2:
        #    elem
        #else:
        elemNegated = elem*-1

        #print (elemNegated,"elem Negated")
        #applyRules(arrayInFormat, lines, cols, greyFields)
        isPossible = readFile.readPicosatWithArgs(str(elemNegated))
        if (isPossible == 1):
            randomChoice = random.choice((-1, 1))
            writeFile.writeCNF(lits, 1, [[elem* randomChoice]], "a")
            counter += 1
            if(elem* randomChoice > 0):
                #print (elem)
                arrayInFormat[elem//lineNumber][elem%colNumber] = 1
            else:
                arrayInFormat[elem//lineNumber][elem%colNumber] = 2'''
    return data


if __name__ == "__main__":
    #array = []
    #arrayLength = 18
    #for i in range(1,arrayLength+1):
    #    array.append(i)
    #testNeg = buildAllPossibleNegationsIterative(len(array)//2-1, len(array), array)
    impossible = 1
    while impossible:
        try:
            buildNewGrid(8,8)
            impossible = 0
        except:
            impossible = 1



