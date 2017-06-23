#!/usr/bin/python3

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)


continuer = 1
while continuer:
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    pygame.display.flip()

    quit_game = 0
    quit_menu = 0

    while quit_menu != 1:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                quit_menu = 1
                quit_game = 1
                continuer = 0
                maptxt = 0

            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    quit_menu = 1
                    maptxt = 'src/client/gui/n1'


    texture = Texture()
    if maptxt != 0:
        fond = texture.herbe_haute

        carte = Map(maptxt)
        carte.generer()
        carte.afficher(fenetre)
        link = Perso(texture.droite, texture.gauche,
                     texture.haut, texture.bas, carte)


    while quit_game != 1:

        pygame.time.Clock().tick(30)
        #son = pygame.mixer.Sound("src/client/gui/assets/main_theme.wav")
        #son.play()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_menu = 1
                continuer = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game = 1
                elif event.key == K_RIGHT:
                    link.move('droite')
                elif event.key == K_LEFT:
                    link.move('gauche')
                elif event.key == K_UP:
                    link.move('haut')
                elif event.key == K_DOWN:
                    link.move('bas')
        fenetre.blit(fond, (0,0))
        carte.afficher(fenetre)
        fenetre.blit(link.direction, (link.x, link.y))
        pygame.display.flip()
