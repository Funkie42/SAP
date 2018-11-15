import subprocess

# read the data form the game.txt file
# returns the amount of columns and lines and the gamefield in form [[x1,x2,...,xn],[],[],...,[]]
# 2 = back block
# 1 = white block
# 0 = grey block
def readFileData(fileName):
    fo = open(fileName)

    line = fo.readline()
    # array with the game:
    # ? = 0, W = 1, B = 2
    gameboard = []
    nonPerdeterminedFields = []
    cnt = 1
    cols = 0
    lines = 0
    counter = -1
    #loop through the file and create the gameboard
    while line:
        if(cnt >1):
            gameline = []

            width = len(line)
            for i in line:
                counter += 1
                if i == "?":
                    gameline.append(0)
                    nonPerdeterminedFields.append(counter)
                if i == "W":
                    gameline.append(1)
                if i == "B":
                    gameline.append(2)
                if i == "\n":
                    counter -= 1

            gameboard.append(gameline)
        line = fo.readline()
        cnt += 1

    height = cnt - 2
    cols = width - 1
    #print(nonPerdeterminedFields)

    game = {'game': gameboard, 'lines': height, 'cols': cols, 'greyFields': nonPerdeterminedFields}

    return game

# runs picosat and returns the solution
def readPicosatSolution(cols, lines, displayResult = 1):
    result = subprocess.run(['picosat', 'satTest.cnf'], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').splitlines()
    # remove the frist line
    result.pop(0)
    values = []
    for i in result:
        z = i.split()
        for j in z:
            if(j!="v"):
                values.append(j)
    sack = []
    counter = 0
    if displayResult == 0:
        for i in range(len(values)):
            values[i] = int(values[i])
        return values
    if displayResult == 1:
        for i in range(lines):
            minisack = []
            #if displayResult:
            for j in range(cols):
                # negative value = Black = 2
                #print(values)
                if int(values[counter]) < 0:
                    minisack.append(2)
                # positive value = White = 1
                if int(values[counter]) > 0:
                    minisack.append(1)
                counter = counter +1
            sack.append(minisack)
            #else:
            #    return values
        #print(sack)
        return sack
    if displayResult == 2:
        doubleArr = []
        for i in range(lines):
            singleArr = []
            for j in range(cols):
                singleArr.append(int(values[lines*(i)+j-1]))
            doubleArr.append(singleArr)
        return doubleArr

# runs picosat with an additional argument and returns 1 if there is a solutions
# and returns 0 if there is no solution
def readPicosatWithArgs(clause):
    #call picosat with extra clause
    #print (clause,"clause")
    result = subprocess.run(['picosat', '-a',clause , 'satTest.cnf'], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8').splitlines()
    result = result.pop(0)
    if(result == "s SATISFIABLE"):
        # we have to add this term to the formular as a given clause
        return 1
    return 0



if __name__ == "__main__":
    # code for calling picosat
    readPicosatWithArgs("1024")