#!/usr/bin/python3

import pygame
from pygame.locals import *

from classes import *
from constantes import *
from GUI import *


def splash_screen(loop):
    while loop.quitter_menu != True:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                loop.quitter_menu = True
                loop.quitter_jeu = True
                loop.continuer = False
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    loop.quitter_menu = 1

def main_loop(loop, fenetre, carte, link):
    texture = Texture()
    while loop.quitter_jeu != True:
        pygame.time.Clock().tick(30)
        #son = pygame.mixer.Sound("src/client/gui/assets/main_theme.wav")
        #son.play()
        for event in pygame.event.get():
            if event.type == QUIT:
                loop.quitter_jeu = True
                loop.continuer = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop.quitter_jeu = True
                    loop.continuer = False
                elif event.key == K_RIGHT:
                    link.move("droite")
                elif event.key == K_LEFT:
                    link.move("gauche")
                elif event.key == K_UP:
                    link.move("haut")
                elif event.key == K_DOWN:
                    link.move("bas")
        fenetre.blit(texture.herbe_haute, (0,0))
        carte.afficher(fenetre)
        fenetre.blit(link.direction, (link.x, link.y))
        pygame.display.flip()

def main():
    pygame.init()

    fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
    pygame.display.set_caption(titre_fenetre)

    loop = Loop()
    texture = Texture()
    carte = Map("src/client/gui/n1")
    link = Perso(texture.droite, texture.gauche, texture.haut, texture.bas, carte)
    accueil = pygame.image.load(image_accueil).convert()

    fenetre.blit(accueil, (0, 0))

    pygame.display.flip()

    splash_screen(loop)

    carte.generer()
    carte.afficher(fenetre)

    main_loop(loop, fenetre, carte, link)

main()