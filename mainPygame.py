import os
from maze import *
import pygame
from pygame.locals import *

scale = 50
WINSIZE = (Cell.w * scale, Cell.h * scale)
graph = []
fixpos = 0
pos = [0, 0]

def cleanGraph():
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if type(graph[i][j].status) == str:
                graph[i][j] = graph[i][j].status
            else:
                graph[i][j] = "#" if graph[i][j].status else "."
    
def resetAllCell():
    for i in graph:
        for j in i:
            j.reset = True

def drawAll(screen):
    for i in graph:
        for j in i:
            j.draw(screen)

def sometest(screen):

    for i in range(scale):
        temp = []
        for j in range(scale):
            x = Cell(i, j, 0)
            temp.append(x)
        graph.append(temp)

    drawAll(screen)


def Maze():
    pygame.init()
    scr_inf = pygame.display.Info()
    os.environ['SDL_VIDEO_WINDOW_POS'] = '{}, {}'.format(scr_inf.current_w // 2 - WINSIZE[0] // 2,
                                                         scr_inf.current_h // 2 - WINSIZE[1] // 2)
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('PathFinder-GUI')
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    

    sometest(screen)
    fixpos = 0
    pos = [0 , 0]
    done = 0
    while not done:
        for e in pygame.event.get():
            
            xcor, ycor = pygame.mouse.get_pos()
            xcor, ycor = xcor//Cell.w, ycor//Cell.h
            if pygame.mouse.get_pressed()[0]: 
                if  fixpos == 0:
                    fixpos += 1
                    pos[0] = (xcor, ycor)
                    print(start, xcor, ycor, fixpos)
                    graph[xcor][ycor].status = "S"
                    graph[xcor][ycor].changeColor(start)

                elif fixpos == 1 and (xcor, ycor) not in pos:
                    pos[1] = (xcor, ycor)
                    print(end, xcor, ycor)
                    fixpos += 1
                    graph[xcor][ycor].status = "E"
                    graph[xcor][ycor].changeColor(end)

                elif (xcor, ycor) not in pos:
                    graph[xcor][ycor].toggleOn()
                drawAll(screen)

            elif pygame.mouse.get_pressed()[2] and (xcor, ycor) not in pos:    
                graph[xcor][ycor].toggleOff()
                drawAll(screen)

            elif pygame.mouse.get_pressed()[1]:    
                for i in graph:
                    for j in i:
                        j.toggleOff()
                fixpos = 0
                pos = [0 , 0]
                drawAll(screen)

            elif e.type == pygame.MOUSEBUTTONUP:
                resetAllCell()

            elif e.type == KEYDOWN and e.key == K_RETURN :
                cleanGraph()
                pygame.display.flip()
                pygame.quit()
                return graph

            elif e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1

        pygame.display.update()
        clock.tick()


if __name__ == '__main__':
    Maze()