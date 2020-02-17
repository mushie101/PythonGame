import pygame
run=True
pygame.init()
win=pygame.display.set_mode((750,750))
pygame.display.set_caption("River cross 1 v 1")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
    win.fill((0,0,0))



