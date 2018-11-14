import readFile
import writeFile
import interface
import math

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
                arrayOfCurrentRowIndexes.append(data[i * lineNumber + j])
            else:
                arrayOfCurrentRowIndexes.append(data[j * lineNumber + i])
        whiteBlocks = []
        blackBlocks = []
        for elem in arrayOfCurrentRowIndexes:
            #print(elem)
            #print(arrayOfCurrentRowIndexes)

            if elem > 0:
                whiteBlocks.append(elem)
            elif elem < 0:
                blackBlocks.append(elem)

        surplusOfWhiteBlocks = len(whiteBlocks) - len(arrayOfCurrentRowIndexes)//2
        #print(surplusOfWhiteBlocks)
        #print(whiteBlocks)
        if surplusOfWhiteBlocks < 0:
            sack = [[]]
            for i in blackBlocks:
                sack[0].append(i*-1)
            return sack
            print("niga",blackBlocks)
            solutions = buildAllPossibleNegationsIterative(surplusOfWhiteBlocks*-1, len(blackBlocks), blackBlocks, 1)
        elif surplusOfWhiteBlocks > 0:
            sack = [[]]
            for i in whiteBlocks:
                sack[0].append(i*-1)
            print("sack",sack)
            return sack
            #return sack
            #solutions = buildAllPossibleNegationsIterative(surplusOfWhiteBlocks, len(whiteBlocks), whiteBlocks, 0)
            #print("solutions: ", solutions)
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
        #print("negnumb",numbersToNeg)

        #Main loop to write each possibility
        calculating = 1
        while calculating:


            newCNF = arrayOfLineData.copy()


            #LENGTH of array to flip numbers
            for number in numbersToNeg:
                #print("flipped number:",number-1)

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

    #print("first: ",cnfOfLineCheckArray)
    for j in range(len(cnfOfLineCheckArray[0])):
       cnfOfLineCheckArray[0][j] = cnfOfLineCheckArray[0][j] * -1
    #print ("second: ", cnfOfLineCheckArray)

    return cnfOfLineCheckArray

#RECURSIVE! VERY INEFFICENT!
#returns all pos and negativ possibility for a given amout of negations and variables
def buildAllPossibleNegationsRecursive(negationAmout, varAmount, arrayOfLineData, changedNumbers = []):
    #global counter
    #counter += 1
    #print(counter)
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
    #print(len(solutions))
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
            print("line: ", i, "col: ", j, "data: ", data[i * lineNumber + j])
            if(data[i * lineNumber + j] > 0):
                counter = counter + 1
        print("counter: ", counter, "lineNumber: ", lineNumber)
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

def applyRules(data, lines, cols, greyFields):
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
        print("I: ", i)
    # we have found the perfect solution but now exclude all other possibilities
    # herefor we got throug everystone and check if it could be switched
    # if so we have to write this stone in our satfile
    checkEveryStoneForOtherSolutions(data, greyFields)
    print(data)


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
def checkEveryStoneForOtherSolutions(data, greyFields):

    lits = colNumber * lineNumber
    counter = 0
    for elem in greyFields:
        print(counter)
        counter += 1
        #check it for the negative value if it would be possible in other solution
        elem = data[elem]*-1
        isPossible = readFile.readPicosatWithArgs(str(elem))
        if(isPossible==1):
            elem = elem*-1
            #it can be switched and therefor this possibility has to be excluded
            writeFile.writeCNF(lits, 1, [[elem]], "a")





if __name__ == "__main__":
    array = []
    arrayLength = 18
    for i in range(1,arrayLength+1):
        array.append(i)
    testNeg = buildAllPossibleNegationsIterative(len(array)//2-1, len(array), array)
    #print(testNeg)
