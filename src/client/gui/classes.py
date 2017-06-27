#!/usr/bin/python3

import sys
import pygame
from pygame.locals import *
from constantes import *
import random


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Loop:
    def __init__(self):
        self.quitter_jeu = False
        self.quitter_menu = False
        self.continuer = True


class Color(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


class SpriteSheet:
        def __init__(self, file_name):
                pygame.init()
                #pygame.display.set_caption(titre_fenetre)
                #window = pygame.display.set_mode((600, 1000))
                self.sprite_sheet = pygame.image.load(file_name).convert()

        def get_image(self, x, y, width, height, color):
                image = pygame.Surface([width, height]).convert()
                image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
                image.set_colorkey(color)
                return image


class Texture(object):
        def __init__(self):
                color = Color()

                herbe = SpriteSheet("src/client/gui/assets/tileset_world.png")
                image_herbe_basse = herbe.get_image(253, 57, 16, 16, color.BLACK)
                image_herbe_haute = herbe.get_image(270, 57, 16, 16, color.BLACK)
                self.herbe_basse = pygame.transform.scale(image_herbe_basse, (48, 48))
                self.herbe_haute = pygame.transform.scale(image_herbe_haute, (48, 48))

                rubis = SpriteSheet("src/client/gui/assets/tileset_rubis.png")
                image_rubis_vert = rubis.get_image(167, 363, 30, 48, color.WHITE)
                image_rubis_bleu = rubis.get_image(195, 363, 30, 48, color.WHITE)
                image_rubis_jaune = rubis.get_image(223, 363, 30, 48, color.WHITE)
                image_rubis_rouge = rubis.get_image(251, 363, 30, 48, color.WHITE)
                image_rubis_violet = rubis.get_image(278, 363, 30, 48, color.WHITE)
                image_rubis_orange = rubis.get_image(305, 363, 30, 48, color.WHITE)
                self.rubis_vert = pygame.transform.scale(image_rubis_vert, (12, 24))
                self.rubis_bleu = pygame.transform.scale(image_rubis_bleu, (12, 24))
                self.rubis_jaune = pygame.transform.scale(image_rubis_jaune, (12, 24))
                self.rubis_rouge = pygame.transform.scale(image_rubis_rouge, (12, 24))

                self.rubis_violet = pygame.transform.scale(image_rubis_violet, (12, 24))
                self.rubis_orange = pygame.transform.scale(image_rubis_orange, (12, 24))

                linkvert = SpriteSheet("src/client/gui/assets/persos.png")
                bas = linkvert.get_image(222, 485, 25, 25, color.BLACK)
                droite = linkvert.get_image(197, 453, 25, 25, color.BLACK)
                gauche = linkvert.get_image(10, 453, 25, 25, color.BLACK)
                haut = linkvert.get_image(10, 486, 25, 25, color.BLACK)
                self.bas = pygame.transform.scale(bas, (48, 48))
                self.droite = pygame.transform.scale(droite, (48, 48))
                self.gauche = pygame.transform.scale(gauche, (48, 48))
                self.haut = pygame.transform.scale(haut, (48, 48))

                eau = SpriteSheet("src/client/gui/assets/eau.png")
                bord = eau.get_image(303, 863, 15, 15, color.BLACK)
                self.bord = pygame.transform.scale(bord, (48, 48))


class Map:
    def __init__(self, sprite_width, sprite_height):
        self.map = []
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.width = sprite_width // 48
        self.height = sprite_height // 48

        color = Color()
        herbe = SpriteSheet("src/client/gui/assets/tileset_world.png")
        image_herbe_basse = herbe.get_image(253, 57, 16, 16, color.BLACK)
        image_herbe_haute = herbe.get_image(270, 57, 16, 16, color.BLACK)
        self.herbe_basse = pygame.transform.scale(image_herbe_basse, (48, 48))
        self.herbe_haute = pygame.transform.scale(image_herbe_haute, (48, 48))


    def create(self, window):
        cell = {'texture':self.herbe_haute, 'food':0}
        self.map = [[{} for x in range(self.width)] for y in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                cell = {
                    'texture':  self.herbe_haute,
                    'food':     y * self.width + x,
                }
                self.map[y][x] = cell
        print("onEggHatch egg_num={}".format(self.map))

        """
        try:
            file = open("map.txt", 'w+')
        except IOError:
            pass
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    file.write("o")
                else:
                    if random.randint(0, 1) == 0:
                        file.write(".")
                    else:
                        file.write(",")
            file.write("\n")
        """

    def read(self, window):
        """
        try:
            file = open("map.txt", 'r')
        except IOError:
            pass
        texture = Texture()
        herbe_basse = texture.herbe_basse
        herbe_haute = texture.herbe_haute
        bord = texture.bord
        """

        for x in range(self.width):
            for y in range(self.height):
                window.blit(self.map[y][x]['texture'], (x * 48, y * 48))

        """
        for i in range(self.height):
            for j in range(self.width + 1):
                c = file.read(1)
                if c == "o":
                    window.blit(bord, (j * 48, i * 48))
                elif c == ".":
                    window.blit(herbe_haute, (j * 48, i * 48))
                elif c == ",":
                    window.blit(herbe_basse, (j * 48, i * 48))
        """


class PlayerList:
    def __init__(self):
        self.list = []

    def display_players(self, window):
        for i in range(len(self.list)):
            player = self.list[i]
            window.blit(player.direction, (player.x, player.y))

    def get_player(self, player_num):
        i = 0
        for player in self.list:
            if int(player.player_num) == int(player_num):
                return i
            i += 1
        return i

    def add_player(self, player):
        self.list.append(player)

    def remove_player(self, player_num):
        i = 0
        for player in self.list:
            if int(player.player_num) == int(player_num):
                self.list.pop(i)
            i += 1


class Perso:
    def __init__(self, player_num, team, model, map):
        self.team = team
        self.player_num = player_num
        self.level = 1
        self.model = model
        self.case_x = 1
        self.case_y = 1
        self.x = 1
        self.y = 1
        self.direction = 0
        self.droite = 0
        self.gauche = 0
        self.bas = 0
        self.haut = 0
        self.map = map

    def assign_model(self):
        color = Color()
        if self.model == 0:
            linkvert = SpriteSheet("src/client/gui/assets/persos.png")
            bas = linkvert.get_image(222, 485, 25, 25, color.BLACK)
            droite = linkvert.get_image(197, 453, 25, 25, color.BLACK)
            gauche = linkvert.get_image(10, 453, 25, 25, color.BLACK)
            haut = linkvert.get_image(10, 486, 25, 25, color.BLACK)
            self.bas = pygame.transform.scale(bas, (48, 48))
            self.droite = pygame.transform.scale(droite, (48, 48))
            self.gauche = pygame.transform.scale(gauche, (48, 48))
            self.haut = pygame.transform.scale(haut, (48, 48))

    def set_direction(self, orientation):
        if orientation == 1:
            self.direction = self.bas
        elif orientation == 2:
            self.direction = self.droite
        elif orientation == 4:
            self.direction = self.gauche
        elif orientation == 3:
            self.direction = self.haut

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
