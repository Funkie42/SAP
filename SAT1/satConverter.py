import readFile
import writeFile

def convertToSat():
    # Read input data to Array "data"
    data = readFile.readFileData()
    print(data)

    '''
    TODO LOGIC TO convert to CNF
    
    
    '''
    cnf = [[1,-3],[2,3,-1]] #Dummy version

    #number of literals and terms

    lits = 3
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