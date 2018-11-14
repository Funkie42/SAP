import pygame
import readFile
import satConverter
import subprocess

rectSize = 50

#init colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (133, 133, 133)
backgroundWhite = (222, 222, 222)

#Read input data to Array "data"
gameData = readFile.readFileData('./ueb1/u01puzzle-huge1.txt')
data = gameData['game']
cols = gameData['cols']
lines = gameData['lines']



def drawGrit(cols, lines, data):
    for i in range(0,lines):
        for j in range (0,cols):

            #for unsolved blocks
            if (data[j][i] == 0):
                pygame.draw.rect(screen, gray, pygame.Rect((i*rectSize, j*rectSize), (rectSize-1, rectSize-1)))
            #for white blocks
            if (data[j][i] == 1):
                pygame.draw.rect(screen, white, pygame.Rect((i * rectSize, j * rectSize), (rectSize - 1, rectSize - 1)))
            #for black blocks
            if (data[j][i] == 2):
                pygame.draw.rect(screen, black, pygame.Rect((i * rectSize, j * rectSize), (rectSize - 1, rectSize - 1)))

if __name__ == "__main__":
    pygame.init()
    size = [cols*rectSize-1, lines*rectSize-1]
    screen=pygame.display.set_mode(size)
    pygame.display.set_caption("SAT 1 - Unruly")
    done = False
    clock = pygame.time.Clock()
    fractal_level = 1

    while done is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # code for calling picosat

                    #apply the rule for the 3 solver
                    satConverter.convertToSat(data)
                    data = readFile.readPicosatSolution(cols, lines, 0)
                    # call the code to add clauses for amount restriction
                    satConverter.convertToSat(data,1)
                    data = readFile.readPicosatSolution(cols, lines,0)
                    print("öfkasdjö ", data)
                    puzzleSolved = 0
                    i = 0
                    while( puzzleSolved == 0):
                        satConverter.convertToSat(data, 1)
                        data = readFile.readPicosatSolution(cols, lines, 0)
                        # check if equal amount in al rows
                        puzzleSolved = satConverter.checkIfDataIsDevineLines(data, cols, lines)
                        if (puzzleSolved == 1):
                            #check if all rows are equal
                            puzzleSolved = satConverter.checkIfDataIsDevineCols(data, cols, lines)
                            #satConverter.convertToSat(data, 1)
                            data = readFile.readPicosatSolution(cols, lines, 0)

                        i = i+1
                        print("I: ",i)
                    # we have a solution and can display it
                    satConverter.convertToSat(data, 1)
                    data = readFile.readPicosatSolution(cols, lines, 0)
                    satConverter.convertToSat(data, 1)
                    data = readFile.readPicosatSolution(cols, lines, 0)
                    print(data)
                    sol = []
                    counter = 0
                    for i in range(lines):
                        subSol = []
                        for j in range(cols):
                            if(data[counter] < 0):
                                subSol.append(2)
                            else:
                                subSol.append(1)
                            counter += 1
                        sol.append(subSol)
                    print("subSol: ", sol)

                    #data = readFile.readPicosatSolution(cols, lines, 1)
                    data = sol

                    print(data)
        screen.fill(backgroundWhite)
        drawGrit(cols, lines, data)

        clock.tick(20)
        pygame.display.flip()

    pygame.quit ()