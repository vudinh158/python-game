import pygame
import sys
from GameBlockPuzzle import draw_text_middle, main_menu,s_width,s_height

strStart = "Press Any Key To Play"

def main(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle(win, strStart, 60, (255, 255, 255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main_menu(win)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Block Puzzle')
main(win)