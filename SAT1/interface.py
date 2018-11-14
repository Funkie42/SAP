import pygame
import readFile
import satConverter
import subprocess
import os

filenames = []
filenames.append("Random File Size 4")
filenames.append("Random File Size 8")
filenames.append("Random File Size 14")
filnamePosition = -1
for root, dirs, files in os.walk("./ueb1"):
    for filename in files:
        if filename[-1] == "t":
            filenames.append(filename)




pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 18)

chooseGameText = "Press down to find possible levels"

#init colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (133, 133, 133)
backgroundWhite = (222, 222, 222)

#Read input data to Array "data"
gameData = readFile.readFileData('./ueb1/' + filenames[-1])
data = gameData['game']
cols = gameData['cols']
lines = gameData['lines']
greyFields = gameData['greyFields']

menuHight = 30
gameSize = [900, 900]

rectwidth = gameSize[0]/cols
recthight = gameSize[1]/lines




def drawGrit(cols, lines, data):
    for i in range(0,lines):
        for j in range (0,cols):

            #for unsolved blocks
            if (data[j][i] == 0):
                pygame.draw.rect(screen, gray, pygame.Rect((i*rectwidth, j*recthight), (rectwidth-1, recthight-1)))
            #for white blocks
            if (data[j][i] == 1):
                pygame.draw.rect(screen, white, pygame.Rect((i * rectwidth, j * recthight), (rectwidth - 1, recthight - 1)))
            #for black blocks
            if (data[j][i] == 2):
                pygame.draw.rect(screen, black, pygame.Rect((i * rectwidth, j * recthight), (rectwidth - 1, recthight - 1)))

if __name__ == "__main__":



    pygame.init()
    size = [gameSize[0], gameSize[1] + menuHight]
    screen=pygame.display.set_mode(size,pygame.RESIZABLE)
    pygame.display.set_caption("SAT 1 - Unruly")
    done = False
    clock = pygame.time.Clock()
    fractal_level = 1

    chooseGameTextsurface = myfont.render(chooseGameText, 0, black)

    while done is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # code for calling picosat
                    data = satConverter.applyRules(data, lines, cols, greyFields)

                #choose level to play
                if event.key == pygame.K_DOWN:
                    filnamePosition += 1
                    if filnamePosition == len(filenames):
                        filnamePosition = 0
                    chooseGameText = filenames[filnamePosition]
                    chooseGameTextsurface = myfont.render("Play: " + chooseGameText + "? Press Enter!", 0, black)

                #confirm level to play
                if event.key == pygame.K_RETURN:
                    if filnamePosition < 3:
                        cols = 8
                        lines = 8
                        impossible = 1
                        while impossible: #if random solution is impossible, try again

                            dataOfRandomGame = satConverter.buildNewGrid(cols, lines)
                            counter = 0
                            greyFields = []
                            for i in gameData:
                                for j in i:
                                    if j == 0:
                                        greyFields.append(counter)
                                    counter += 1

                            gameData = {'game': dataOfRandomGame, 'lines': lines, 'cols': cols, 'greyFields': greyFields}

                            impossible = 0

                    else:
                        gameData = readFile.readFileData('./ueb1/' + filenames[filnamePosition])

                    data = gameData['game']
                    cols = gameData['cols']
                    lines = gameData['lines']
                    greyFields = gameData['greyFields']

                    #print("data",data)
                    #print("gameData",gameData)

                    rectwidth = gameSize[0] // cols
                    recthight = gameSize[1] // lines
                    chooseGameTextsurface = myfont.render("Playing: " + chooseGameText, 0, black)



            if event.type == pygame.USEREVENT and event.code == 'MENU':
                print ('menu event: %s.%d: %s' % (event.name, event.item_id, event.text))


        screen.fill(backgroundWhite)
        drawGrit(cols, lines, data)
        screen.blit(chooseGameTextsurface, (10, recthight*lines))

        clock.tick(20)

        pygame.display.flip()

    pygame.quit()