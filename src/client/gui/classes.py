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


class Resource:
    g_instance = None

    @staticmethod
    def instance():
        if Resource.g_instance is None:
            Resource.g_instance = Resource()
        return Resource.g_instance

    def __init__(self):
        color = Color()

        rubis = SpriteSheet("src/client/gui/assets/tileset_rubis.png")
        image_rubis_vert = rubis.get_image(167, 363, 30, 48, color.WHITE)
        image_rubis_bleu = rubis.get_image(195, 363, 30, 48, color.WHITE)
        image_rubis_jaune = rubis.get_image(223, 363, 30, 48, color.WHITE)
        image_rubis_rouge = rubis.get_image(251, 363, 30, 48, color.WHITE)
        image_rubis_violet = rubis.get_image(278, 363, 30, 48, color.WHITE)
        image_rubis_orange = rubis.get_image(305, 363, 30, 48, color.WHITE)
        self.rubis_vert = pygame.transform.scale(image_rubis_vert, (8, 16))
        self.rubis_bleu = pygame.transform.scale(image_rubis_bleu, (8, 16))
        self.rubis_jaune = pygame.transform.scale(image_rubis_jaune, (8, 16))
        self.rubis_rouge = pygame.transform.scale(image_rubis_rouge, (8, 16))
        self.rubis_violet = pygame.transform.scale(image_rubis_violet, (8, 16))
        self.rubis_orange = pygame.transform.scale(image_rubis_orange, (8, 16))

    def display_linemate(self, window, coordLinemate):
        if coordLinemate.nb_resource > 0:
            window.blit(self.rubis_vert, (coordLinemate.case_x, coordLinemate.case_y))

    def display_deraumere(self, window, coordDeraumere):
        if coordDeraumere.nb_resource > 0:
            window.blit(self.rubis_bleu, (coordDeraumere.case_x, coordDeraumere.case_y))

    def display_sibur(self, window, coordSibur):
        if coordSibur.nb_resource > 0:
            window.blit(self.rubis_jaune, (coordSibur.case_x, coordSibur.case_y))

    def display_mendiane(self, window, coordMendiane):
        if coordMendiane.nb_resource > 0:
            window.blit(self.rubis_rouge, (coordMendiane.case_x, coordMendiane.case_y))

    def display_phiras(self, window, coordPhiras):
        if coordPhiras.nb_resource > 0:
            window.blit(self.rubis_violet, (coordPhiras.case_x, coordPhiras.case_y))

    def display_thystame(self, window, coordThystame):
        if coordThystame.nb_resource > 0:
            window.blit(self.rubis_orange, (coordThystame.case_x, coordThystame.case_y))


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class CoordResource:
    def __init__(self, nb_resource, x, y):
        self.x = x
        self.y = y
        self.nb_resource = nb_resource
        self.case_x = random.randint(0, 36) + self.x * 48
        self.case_y = random.randint(0, 24) + self.y * 48

    def set_nb_resource(self, nb_resource):
        self.nb_resource = nb_resource


class Map:
    def __init__(self, sprite_width, sprite_height):
        self.map = []
        self.stone_map = []
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.width = sprite_width // 48
        self.height = sprite_height // 48
        self.resource = Resource.instance()

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

        coordResource = CoordResource(-1, -1, -1)
        for y in range(self.height):
            for x in range(self.width):
                index = 0 if random.randint(0, 100) <= 75 else random.randint(1, len(self.Ground) - 1)
                cell = {
                    'texture':  self.Ground[index],
                    'food':     coordResource,
                    'linemate': coordResource,
                    'deraumere': coordResource,
                    'sibur': coordResource,
                    'mendiane': coordResource,
                    'phiras': coordResource,
                    'thystame': coordResource
                }
                self.map[y][x] = cell
        print("onEggHatch egg_num={}".format(self.map))

    def check_if_resource_exist(self, coord_precedent, coord_next):
        if coord_precedent.nb_resource > -1:
            coord_precedent.set_nb_resource(coord_next.nb_resource)
        else:
            return coord_next
        return coord_precedent

    def add_case_content(self, x, y, resources):
        coordLinemate = CoordResource(resources['linemate'], x, y)
        self.map[y][x]['linemate'] = self.check_if_resource_exist(self.map[y][x]['linemate'], coordLinemate)
        coordDeraumere = CoordResource(resources['deraumere'], x, y)
        self.map[y][x]['deraumere'] = self.check_if_resource_exist(self.map[y][x]['deraumere'], coordDeraumere)
        coordSibur = CoordResource(resources['sibur'], x, y)
        self.map[y][x]['sibur'] = self.check_if_resource_exist(self.map[y][x]['sibur'], coordSibur)
        coordMendiane = CoordResource(resources['mendiane'], x, y)
        self.map[y][x]['mendiane'] = self.check_if_resource_exist(self.map[y][x]['mendiane'], coordMendiane)
        coordPhiras = CoordResource(resources['phiras'], x, y)
        self.map[y][x]['phiras'] = self.check_if_resource_exist(self.map[y][x]['phiras'], coordPhiras)
        coordThystame = CoordResource(resources['thystame'], x, y)
        self.map[y][x]['thystame'] = self.check_if_resource_exist(self.map[y][x]['thystame'], coordThystame)

    def display_content(self, window):
        for i in range(self.height):
            for j in range(self.width):
                self.resource.display_linemate(window, self.map[i][j]['linemate'])
                self.resource.display_deraumere(window, self.map[i][j]['deraumere'])
                self.resource.display_sibur(window, self.map[i][j]['sibur'])
                self.resource.display_mendiane(window, self.map[i][j]['mendiane'])
                self.resource.display_phiras(window, self.map[i][j]['phiras'])
                self.resource.display_thystame(window, self.map[i][j]['thystame'])

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
