import pygame
import readFile
import satConverter

rectSize = 50

#init colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (133, 133, 133)
backgroundWhite = (222, 222, 222)

#Read input data to Array "data"
gameData = readFile.readFileData('./ueb1/2x2.txt')
data = gameData['game']
cols = gameData['cols']
lines = gameData['lines']



def drawGrit(cols, lines, data):
    for i in range(0,cols):
        for j in range (0,lines):

            #for unsolved blocks
            if (data[i][j] == 0):
                pygame.draw.rect(screen, gray, pygame.Rect((i*rectSize, j*rectSize), (rectSize-1, rectSize-1)))
            #for white blocks
            if (data[i][j] == 1):
                pygame.draw.rect(screen, white, pygame.Rect((i * rectSize, j * rectSize), (rectSize - 1, rectSize - 1)))
            #for black blocks
            if (data[i][j] == 2):
                pygame.draw.rect(screen, black, pygame.Rect((i * rectSize, j * rectSize), (rectSize - 1, rectSize - 1)))


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

        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fractal_level += 1
            if event.key == pygame.K_DOWN:
                fractal_level -= 1

        if fractal_level < 0 or fractal_level > 10:
            fractal_level = 0'''

    screen.fill(backgroundWhite)
    drawGrit(cols, lines, data)
    clock.tick(20)
    pygame.display.flip()

pygame.quit ()