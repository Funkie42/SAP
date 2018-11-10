import readFile
import writeFile
import interface

def writeNumbersInFormat(line, colmun, colNumber):

    numberToBeAdded = str((line)*colNumber+colmun+1)
    return numberToBeAdded

def addSantaClauses(line,column,colNumber):

    hoehoehoe = []

    # Check Lines for 50/50 distribution
    '''cnf.append([writeNumbersInFormat(i,j,data)])'''

    # Check Columns for 50/50 distribution

    # Check Horizontal 3 in a row

    # left left middle
    #if line > 1:
     #   2-2
    # left middle right
    if (line > 0) & (line < colNumber - 1):
        #loop the clauses and make sure one is always negative
        for i in range(3):
            hoehoehoe.append([writeNumbersInFormat(line, column - 1, colNumber),
                              writeNumbersInFormat(line, column, colNumber),
                              writeNumbersInFormat(line, column + 1, colNumber)])
            hoehoehoe[len(hoehoehoe)-1][i] = "-" + hoehoehoe[len(hoehoehoe)-1][i]

        print(hoehoehoe)

    # middle right right
    if line < colNumber - 2:
        0
    # Check vertical 3 in a row

    return hoehoehoe


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
            if data[i][j] == 1: #Insert white blocks
                cnf.append([writeNumbersInFormat(i, j, colNumber)])

            elif data[i][j] ==2: #Insert black blocks
                cnf.append(["-" + writeNumbersInFormat(i, j, colNumber)])

            #Check only unknown blocks (Grey blocks)
            else:
                # add clauses to determine unknown blocks
                santasHoeCollection = addSantaClauses(i, j, colNumber)
                for whore in santasHoeCollection:
                    cnf.append(whore)





    print(cnf)

    #number of literals and terms

    lits = len(data)*len(data[0])
    terms = len(cnf)

    #write converted CNF to File
    filenameCNF = writeFile.writeCNF(lits, terms, cnf)

    '''TODO'''
    #Open PicoSat and get solution for CNF in Array
    solvedData = usePicoSat(filenameCNF)



#Open PicoSat and get solution for CNF in Array
def usePicoSat(filenameCNF):
    return 0

if __name__ == "__main__":
    convertToSat()