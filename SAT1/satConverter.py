import readFile
import writeFile

def writeNumbersInFormat(yPos, xPos, data):

    numberToBeAdded = str((yPos)*len(data)+xPos+1)

    return numberToBeAdded

def convertToSat():
    # Read input data to Array "data"
    data = readFile.readFileData()

    '''TODO LOGIC TO convert to CNF
    
    '''
    cnf = []

    for i in range(len(data)):
        for j in range(len(data[i])):

            '''Insert given blockcolors as Unit-Terms
            
            White blocks are represented by a positive value
            Black blocks are represented by a negative value
            '''
            if data[i][j] == 1: #Insert white blocks
                cnf.append([writeNumbersInFormat(i, j, data)])

            elif data[i][j] ==2: #Insert black blocks
                cnf.append(["-" + writeNumbersInFormat(i, j, data)])


            #Check Lines for 50/50 distribution
            '''cnf.append([writeNumbersInFormat(i,j,data)])'''

            #Check Columns for 50/50 distribution

            #Check Horizontal 3 in a row

            #Check vertical 3 in a row


    print(cnf)

    '''
    end TODO
    '''
    'cnf = [[1,-3],[2,3,-1]] #Dummy version'

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