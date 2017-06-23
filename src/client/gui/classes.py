#!/usr/bin/python3

import pygame
from pygame.locals import * 
from constantes import *

class Color(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


class SpriteSheet:
        def __init__(self, file_name):
                self.sprite_sheet = pygame.image.load(file_name).convert()
                    
        def get_image(self, x, y, width, height):
                color = Color()
                image = pygame.Surface([width, height]).convert()
                image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
                image.set_colorkey(color.BLACK)
                return image              


class Texture(object):
        def __init__(self):
                spritesheet = SpriteSheet("src/client/gui/assets/tileset_world.png")
                image_herbe_basse = spritesheet.get_image(253, 57, 16, 16)
                image_herbe_haute = spritesheet.get_image(270, 57, 16, 16)
                self.herbe_basse = pygame.transform.scale(image_herbe_basse, (48, 48))
                self.herbe_haute = pygame.transform.scale(image_herbe_haute, (48, 48))
                linkvert = SpriteSheet("src/client/gui/assets/persos.png")
                bas = linkvert.get_image(222, 485, 25, 25)
                droite = linkvert.get_image(197, 453, 25, 25)
                gauche = linkvert.get_image(10, 453, 25, 25)
                haut = linkvert.get_image(10, 486, 25, 25)
                self.bas = pygame.transform.scale(bas, (48, 48))
                self.droite = pygame.transform.scale(droite, (48, 48))
                self.gauche = pygame.transform.scale(gauche, (48, 48))
                self.haut = pygame.transform.scale(haut, (48, 48))
                eau = SpriteSheet("src/client/gui/assets/eau.png")
                bord = eau.get_image(303, 863, 15, 15)
                self.bord = pygame.transform.scale(bord, (48, 48))

class Map:
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0


    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau


    def afficher(self, fenetre):
        texture = Texture()
        basse = texture.herbe_basse
        haute = texture.herbe_haute

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':
                    fenetre.blit(haute, (x,y))
                elif sprite == 'e':
                    fenetre.blit(texture.bord, (x,y))
                else:
                    fenetre.blit(basse, (x,y))
                num_case += 1
            num_ligne += 1




class Perso:
    def __init__(self, droite, gauche, haut, bas, map):
        self.droite = droite
        self.gauche = gauche
        self.haut = haut
        self.bas = bas
        self.case_x = 1
        self.case_y = 1
        self.x = 1
        self.y = 1
        self.direction = self.droite
        self.map = map


    def move(self, direction):

        if direction == 'droite':
            if self.case_x < (nombre_sprite_cote - 1):
                self.case_x += 1
                self.x = self.case_x * taille_sprite
            if self.case_x == (nombre_sprite_cote - 1):
                self.case_x = 1
                self.x = self.case_x * taille_sprite
            self.direction = self.droite

        if direction == 'gauche':
            if self.case_x > 0:
                self.case_x -= 1
                self.x = self.case_x * taille_sprite
            if self.case_x == 0:
                self.case_x = nombre_sprite_cote - 2
                self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        if direction == 'haut':
            if self.case_y > 0:
                self.case_y -= 1
                self.y = self.case_y * taille_sprite
            if self.case_y == 0:
                self.case_y = nombre_sprite_cote - 2
                self.y = self.case_y * taille_sprite
            self.direction = self.haut

        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                self.case_y += 1
                self.y = self.case_y * taille_sprite
            if self.case_y == (nombre_sprite_cote - 1):
                self.case_y = 1
                self.y = self.case_y * taille_sprite
            self.direction = self.bas
