import pygame
import models
import sys


SIZE_X = 50
SIZE_Y = 50
SIZE_RATIO = 15
GRID_SIZE  = 3
GRID_COLOR = (88,88,88)
ALIVE_COLOR = (0,0,0)
DEATH_COLOR = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((SIZE_X*SIZE_RATIO, SIZE_Y*SIZE_RATIO))

table = models.Table((SIZE_X, SIZE_Y))



for line_n in range(SIZE_X):
    # Draw horizontal
    line_y = line_n*SIZE_RATIO + GRID_SIZE*(line_n)
    pygame.draw.line(screen, GRID_COLOR, (0,line_y), (SIZE_X*SIZE_RATIO, line_y), GRID_SIZE)

    # Draw vertical
    line_x = line_n*SIZE_RATIO + GRID_SIZE*(line_n)
    pygame.draw.line(screen, GRID_COLOR, (line_x, 0), (line_x, SIZE_Y*SIZE_RATIO), GRID_SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for y in range(table.size[0]):
        for x in range(table.size[1]):
            cell = table.coords2cell(x,y)
            if cell.is_alive:
                color = ALIVE_COLOR
            else:
                color = DEATH_COLOR

            cell_x = x*SIZE_RATIO + x*GRID_SIZE
            cell_y = y*SIZE_RATIO + y*GRID_SIZE

            pygame.draw.rect(screen, color, pygame.Rect(cell_x, cell_y, SIZE_RATIO, SIZE_RATIO))

    pygame.display.flip()

    table.next_gen()
