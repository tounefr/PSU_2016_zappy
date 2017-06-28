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


class Stone:
    def __init__(self):
        color = Color()

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

    def display_linemate(self, window, coordLinemate):
        for coord in coordLinemate.tab_coord:
            window.blit(self.rubis_vert, (coord.x, coord.y))

    def display_deraumere(self, window, coordDeraumere):
        for coord in coordDeraumere.tab_coord:
            window.blit(self.rubis_bleu, (coord.x, coord.y))

    def display_sibur(self, window, coordSibur):
        for coord in coordSibur.tab_coord:
            window.blit(self.rubis_jaune, (coord.x, coord.y))

    def display_mendiane(self, window, coordMendiane):
        for coord in coordMendiane.tab_coord:
            window.blit(self.rubis_rouge, (coord.x, coord.y))

    def display_phiras(self, window, coordPhiras):
        for coord in coordPhiras.tab_coord:
            window.blit(self.rubis_violet, (coord.x, coord.y))

    def display_thystame(self, window, coordThystame):
        for coord in coordThystame.tab_coord:
            window.blit(self.rubis_orange, (coord.x, coord.y))

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class CoordStone:
    def __init__(self, nb_stone, x, y):
        self.x = x
        self.y = y
        self.nb_stone = nb_stone
        self.tab_coord = []

    def set_coord_stone(self):
        for i in range(self.nb_stone):
            coord = Coord(random.randint(0, 36) + self.x * 48, random.randint(0, 24) + self.y * 48)
            self.tab_coord.append(coord)

    def add(self, nb):
        for i in range(nb):
            coord = Coord(random.randint(0, 36) + self.x * 48, random.randint(0, 24) + self.y * 48)
            self.tab_coord.append(coord)

    def remove(self, nb):
        for i in range(nb):
            del self.tab_coord[i]

class Map:
    def __init__(self, sprite_width, sprite_height):
        self.map = []
        self.stone_map = []
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.width = sprite_width // 48
        self.height = sprite_height // 48
        self.stone = Stone()

        color = Color()
        GroundTexture = SpriteSheet("src/client/gui/assets/terrain.png")
        img_ground0 = GroundTexture.get_image(0, 0, 16, 16, color.BLACK)
        img_ground1 = GroundTexture.get_image(16, 0, 16, 16, color.BLACK)
        img_ground2 = GroundTexture.get_image(32, 0, 16, 16, color.BLACK)
        img_ground3 = GroundTexture.get_image(48, 0, 16, 16, color.BLACK)
        img_ground4 = GroundTexture.get_image(64, 0, 16, 16, color.BLACK)
        img_ground5 = GroundTexture.get_image(80, 0, 16, 16, color.BLACK)
        img_ground6 = GroundTexture.get_image(96, 0, 16, 16, color.BLACK)

        self.Ground = []
        self.Ground.append(pygame.transform.scale(img_ground0, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground1, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground2, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground3, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground4, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground5, (48, 48)))
        self.Ground.append(pygame.transform.scale(img_ground6, (48, 48)))

        """
        herbe = SpriteSheet("src/client/gui/assets/tileset_world.png")
        image_herbe_basse = herbe.get_image(253, 57, 16, 16, color.BLACK)
        image_herbe_haute = herbe.get_image(270, 57, 16, 16, color.BLACK)
        self.herbe_basse = pygame.transform.scale(image_herbe_basse, (48, 48))
        self.herbe_haute = pygame.transform.scale(image_herbe_haute, (48, 48))
        """


    def create(self, window):
        cell = {'texture':self.Ground[0], 'food':0}
        self.map = [[{} for x in range(self.width)] for y in range(self.height)]

        coordStone = CoordStone(-1, -1, -1)
        for y in range(self.height):
            for x in range(self.width):
                index = 0 if random.randint(0, 100) <= 75 else random.randint(1, len(self.Ground) - 1)
                cell = {
                    'texture':  self.Ground[index],
                    'food':     y * self.width + x,
                    'linemate': coordStone,
                    'deraumere': coordStone,
                    'sibur': coordStone,
                    'mendiane': coordStone,
                    'phiras': coordStone,
                    'thystame': coordStone
                }
                self.map[y][x] = cell
        print("onEggHatch egg_num={}".format(self.map))

    def compare_stone(self, coordPrec, coordNext):
        print("\n" + str(coordPrec.nb_stone) + " - " + str(coordNext.nb_stone) + "\n")
        if coordPrec.nb_stone == -1:
            #print("\n\n\n\n----------\n\n\n\n")
            return coordNext
        elif coordPrec.nb_stone == coordNext.nb_stone:
            #print("\n\n\n\n====\n\n\n\n")
            coordNext = coordPrec
        elif coordPrec.nb_stone > coordNext.nb_stone:
            #print("\n\n\n\n>>>>\n\n\n\n")
            nb_stone = coordNext.nb_stone
            coordNext = coordPrec
            coordNext.remove(CoordPrec.nb_stone - nb_stone)
        elif coordPrec.nb_stone < coordNext.nb_stone:
            #print("\n\n\n\n<<<<<<\n\n\n\n")
            nb_stone = coordNext.nb_stone
            coordNext = coordPrec
            coordNext.nb_stone = nb_stone
            coordNext.add(nb_stone - coordPrec.nb_stone)
        return coordNext


    def add_case_content(self, x, y, resources):
        coordLinemate = CoordStone(resources['linemate'], x, y)
        coordLinemate.set_coord_stone()
        self.map[y][x]['linemate'] = self.compare_stone(self.map[y][x]['linemate'], coordLinemate)
        coordDeraumere = CoordStone(resources['deraumere'], x, y)
        coordDeraumere.set_coord_stone()
        self.map[y][x]['deraumere'] = self.compare_stone(self.map[y][x]['deraumere'], coordDeraumere)
        coordSibur = CoordStone(resources['sibur'], x, y)
        coordSibur.set_coord_stone()
        self.map[y][x]['sibur'] = self.compare_stone(self.map[y][x]['sibur'], coordSibur)
        coordMendiane = CoordStone(resources['mendiane'], x, y)
        coordMendiane.set_coord_stone()
        self.map[y][x]['mendiane'] = self.compare_stone(self.map[y][x]['mendiane'], coordMendiane)
        coordPhiras = CoordStone(resources['phiras'], x, y)
        coordPhiras.set_coord_stone()
        self.map[y][x]['phiras'] = self.compare_stone(self.map[y][x]['phiras'], coordPhiras)
        coordThystame = CoordStone(resources['thystame'], x, y)
        coordThystame.set_coord_stone()
        self.map[y][x]['thystame'] = self.compare_stone(self.map[y][x]['thystame'], coordThystame)

    def display_content(self, window):
        for i in range(self.height):
            for j in range(self.width):
                self.stone.display_linemate(window, self.map[i][j]['linemate'])
                self.stone.display_deraumere(window, self.map[i][j]['deraumere'])
                self.stone.display_sibur(window, self.map[i][j]['sibur'])
                self.stone.display_mendiane(window, self.map[i][j]['mendiane'])
                self.stone.display_phiras(window, self.map[i][j]['phiras'])
                self.stone.display_thystame(window, self.map[i][j]['thystame'])

    def read(self, window):
        for x in range(self.width):
            for y in range(self.height):
                window.blit(self.map[y][x]['texture'], (x * 48, y * 48))


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
            character = SpriteSheet("src/client/gui/assets/character.png")
            img_droite = character.get_image(0, 0, 16, 16, color.WHITE)
            img_haut = character.get_image(32, 0, 16, 16, color.WHITE)
            img_gauche = character.get_image(64, 0, 16, 16, color.WHITE)
            img_bas = character.get_image(96, 0, 16, 16, color.WHITE)
            img_take = character.get_image(0, 16, 16, 16, color.WHITE)

            img_death = character.get_image(0, 112, 16, 16, color.WHITE)
            img_layEgg = character.get_image(16, 32, 16, 16, color.WHITE)
            img_egg = character.get_image(0, 48, 16, 16, color.WHITE)
            img_hatch = character.get_image(0, 64, 16, 16, color.WHITE)
            img_incant = character.get_image(0, 80, 16, 16, color.WHITE)
            img_lvlUp = character.get_image(0, 96, 16, 16, color.WHITE)

            self.droite = pygame.transform.scale(img_droite, (48, 48))
            self.haut = pygame.transform.scale(img_haut, (48, 48))
            self.gauche = pygame.transform.scale(img_gauche, (48, 48))
            self.bas = pygame.transform.scale(img_bas, (48, 48))
            self.take = pygame.transform.scale(img_take, (48, 48))

            self.death = pygame.transform.scale(img_death, (48, 48))
            self.layEgg = pygame.transform.scale(img_layEgg, (48, 48))
            self.egg = pygame.transform.scale(img_egg, (48, 48))
            self.hatch = pygame.transform.scale(img_hatch, (48, 48))
            self.incant = pygame.transform.scale(img_incant, (48, 48))
            self.lvlUp = pygame.transform.scale(img_lvlUp, (48, 48))

            """
            linkvert = SpriteSheet("src/client/gui/assets/persos.png")
            bas = linkvert.get_image(222, 485, 25, 25, color.BLACK)
            droite = linkvert.get_image(197, 453, 25, 25, color.BLACK)
            gauche = linkvert.get_image(10, 453, 25, 25, color.BLACK)
            haut = linkvert.get_image(10, 486, 25, 25, color.BLACK)
            self.bas = pygame.transform.scale(bas, (48, 48))
            self.droite = pygame.transform.scale(droite, (48, 48))
            self.gauche = pygame.transform.scale(gauche, (48, 48))
            self.haut = pygame.transform.scale(haut, (48, 48))
            """

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
