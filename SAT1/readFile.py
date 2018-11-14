import subprocess
def readFileData(fileName):
    fo = open(fileName)

    line = fo.readline()
    # array with the game:
    # ? = 0, W = 1, B = 2
    gameboard = []
    cnt = 1
    cols = 0
    lines = 0

    #loop through the file and create the gameboard
    while line:
        if(cnt >1):
            gameline = []
            width = len(line)
            for i in line:
                if i == "?":
                    gameline.append(0)
                if i == "W":
                    gameline.append(1)
                if i == "B":
                    gameline.append(2)
            gameboard.append(gameline)
        line = fo.readline()
        cnt += 1

    height = cnt - 2
    cols = width - 1

    game = {'game': gameboard, 'lines': height, 'cols': cols}

    return game

def readPicosatSolution(cols, lines, displayResult = 1):
    result = subprocess.run(['picosat', 'satTest.cnf'], stdout=subprocess.PIPE)
    #print("Given result:",result)
    result = result.stdout.decode('utf-8').splitlines()
    #print("The given formula is: ", result[0].replace("s ",""))
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

if __name__ == "__main__":
    # code for calling picosat
    x = readPicosatSolution(8,8,2)
    print(x)