'''un  robot può spostarsi su un pavimento con ostacoli; bisogna definire una mappa (in un file csv)
'''
import pygame
from pygame.locals import *

def calc_pav():
    mat = [] 
    with open("percorso.csv", "r") as f:
        for riga in f.readlines():
            riga = riga.split(",")
            mat.append([int(c) for c in riga])
    return mat


def main():

    lato_x = 100
    lato_y = 100
    
    pavimento = calc_pav()
    n_y = len(pavimento)
    n_x = len(pavimento[0])
    k = 1

    pygame.init()
    screen = pygame.display.set_mode((n_x * lato_x , n_y * lato_y))
    muro = pygame.image.load("muro1.png")
    strada = pygame.image.load("strada1.png")
    robot = pygame.image.load("robot.png")
    font = pygame.font.Font(None, 36) 
    
    for riga in pavimento:
        for casella in riga:
            surf1 = pygame.Surface((lato_x, lato_y))
            text = font.render(f"{k}", True, (0,0,0))
            if casella == 1:
                surf1.blit(muro, (0, 0))
                text_pos = text.get_rect(center=(lato_x-50, lato_y-50))  # Regola la posizione del testo
                screen.blit(surf1, (lato_x-100, lato_y-100))  # Sposta l'intera superficie alla posizione corretta
                screen.blit(text, text_pos)
                k += 1
            else:
                surf1.blit(strada, (0, 0))
                screen.blit(surf1, (lato_x-100, lato_y-100))  # Sposta l'intera superficie alla posizione corretta
            
            pygame.display.flip()
            lato_x += 100
            
        lato_x = 100
        lato_y += 100

        screen.blit(robot, (10, 10))
    done = False
    while not done:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                done = True
    pygame.quit()

if __name__ == "__main__":
    main()