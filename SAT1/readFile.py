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

def readPicosatSolution(result):
    print("Given result:",result)
    result = result.stdout.decode('utf-8').splitlines()
    print("The given formula is: ", result[0].replace("s ",""))
    # only take the clauses (written in the second line)
    result = result[1].replace("v ", "").split(" ")
    # result contains all values as string
    lastItem = result[len(result)-2]
    lines = int(lastItem[:2])
    #cols = lastIteint(result[sackCounter])m[2]+lastItem[3]
    cols = 2
    if(lines < 0):
        lines = lines * -1
    if(cols < 0):
        cols = cols * -1
    print(lines)
    sack = []
    sackCounter = 0
    for i in range(lines):
        miniSack = []
        for j in range(cols):
            state = 0
            if(sackCounter > len(result)-1):
                return sack
            if(int(result[sackCounter]) == 0):
                sackCounter = sackCounter +1
                break
            if(int(result[sackCounter]) > 0):
               state = 1  # for white block
            if(int(result[sackCounter]) < 0):
                state = 2 # for black block
            miniSack.append(state)
            sackCounter = sackCounter + 1
        sack.append(miniSack)
    return sack

if __name__ == "__main__":
    # conde for calling picosat
    result = subprocess.run(['picosat', '../picosat-965/simple.cnf'], stdout=subprocess.PIPE)
    x = readPicosatSolution(result)
    print("Result: ", x)