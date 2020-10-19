import os
from maze import *
import pygame
from pygame.locals import *

scale = 41
WINSIZE = (Cell.w * scale, Cell.h * scale)
graph = []



def resetAllCell():
    for i in graph:
        for j in i:
            j.reset = True

def draw_maze(screen):
    maze = Maze(WINSIZE)
    maze.generate(screen, True)

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
    pygame.display.set_caption('harsh shit')
    screen.fill((0, 0, 0))

    clock = pygame.time.Clock()
    

    sometest(screen)

    done = 0
    while not done:
        for e in pygame.event.get():
            
            xcor, ycor = pygame.mouse.get_pos()
            xcor, ycor = xcor//16, ycor//16
            if pygame.mouse.get_pressed()[0]:    
                graph[xcor][ycor].toggleOn()
                drawAll(screen)

            elif pygame.mouse.get_pressed()[2]:    
                graph[xcor][ycor].toggleOff()
                drawAll(screen)

            elif pygame.mouse.get_pressed()[1]:    
                for i in graph:
                    for j in i:
                        j.toggleOff()
                drawAll(screen)

            elif e.type == pygame.MOUSEBUTTONUP:
                resetAllCell()

            elif e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1

        pygame.display.update()
        clock.tick()


if __name__ == '__main__':
    Maze()