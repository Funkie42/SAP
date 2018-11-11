import readFile
import writeFile
import interface

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
def addAmountDistriction(lineNumber, colNumber, vertical):
    sack = []
    for i in range(lineNumber):
        arrayOfCurrentRowIndexes = []
        for j in range(colNumber):
            if vertical:
                arrayOfCurrentRowIndexes.append(i * lineNumber + j + 1)
            else:
                arrayOfCurrentRowIndexes.append(j * lineNumber + i + 1)
        for k in range(colNumber//3,colNumber//2):
            solutions = buildAllPossibleNegations(k, colNumber,arrayOfCurrentRowIndexes, [])
            #print("line: ", i, "   ",k, " :", solutions[0])
            for s in solutions:
                sack.append(s)
    return (sack)

#returns all pos and negativ possibility for a given amout of negations and variables
def buildAllPossibleNegations(negationAmout, varAmount, arrayOfLineData, changedNumbers):
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

        solution = buildAllPossibleNegations(negationAmout-1, varAmount-1, modArray, changedNumbers)
        del changedNumbers[-1]
        #print ("sol",solution)
        #print("change",changedNumber)
        for j in solution:
            solutions.append(j)
    #print("solutions",solutions)
    return solutions


def convertToSat():
    # Read input data to Array "data"
    data = interface.data
    colNumber = len(data[0])
    lineNumber = len(data)

    '''TODO LOGIC TO convert to CNF

    '''
    cnf = []

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

    lineRestictions = addAmountDistriction(lineNumber, colNumber, 1)
    for lineRestiction in lineRestictions:
        cnf.append(lineRestiction)

    colRestictions = addAmountDistriction(colNumber, lineNumber, 0)
    for colRestiction in colRestictions:
        cnf.append(colRestiction)

    # number of literals and terms

    lits = len(data) * len(data[0])
    terms = len(cnf)

    # write converted CNF to File
    filenameCNF = writeFile.writeCNF(lits, terms, cnf)

    '''TODO'''
    # Open PicoSat and get solution for CNF in Array
    solvedData = usePicoSat(filenameCNF)


# Open PicoSat and get solution for CNF in Array
def usePicoSat(filenameCNF):
    return 0


if __name__ == "__main__":
    for i in range(4):
        testNeg = buildAllPossibleNegations(i, 8, [1, 2, 3, 4, 5, 6, 7, 8], [])
    print(i,":  ", testNeg)