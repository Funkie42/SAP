def readFileData():
    fo = open('ueb1/u01puzzle-big1.txt')

    line = fo.readline()
    # array with the game:
    # ? = 0, W = 1, B = 2
    gameboard = []
    cnt = 1
    width = 0
    height = 0

    #loop through the file and create the gameboard
    while line:
        if(cnt == 1):
            print("The game has the measurements: ", line)
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
    width = width - 1

    #print(gameboard)
    return gameboard