import pygame
from random import choice
from random import randint

off = (255, 255, 255)
on =  (34,55,73)
start = ( 242, 208, 21 )
end = ( 255,57,93)

cellstatus = lambda x: on if x else off

class Cell(pygame.sprite.Sprite):
    w, h = 15, 15
    status = 0
    reset = True

    def __init__(self, x, y, status):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([self.w, self.h])
        self.image.fill(cellstatus(status))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.w
        self.rect.y = y * self.h
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (93, 173, 226), self.rect, 1)

    def changeStatus(self):
        self.image.fill(cellstatus(self.status))


    def changeColor(self, color):
        self.image.fill(color)
        
    def toggleOn(self):
        if self.reset:
            self.status = True
            self.changeStatus()
            self.reset = False

    def toggleOff(self):
        if self.reset:
            self.status = False
            self.changeStatus()
            self.reset = False