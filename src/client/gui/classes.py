#!/usr/bin/python3

import sys
import pygame
from pygame.locals import *
from gui.constantes import *
import random


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Teams:
    g_instance = None

    @staticmethod
    def instance():
        if Teams.g_instance is None:
            Teams.g_instance = Teams()
        return Teams.g_instance

    def __init__(self):
        self.list = []
        self.spriteSheet = SpriteSheet("src/client/gui/assets/character.png")
        self.tileDimension = (48, 48)
        self.tileSize = 16

    def getTeam(self, teamName):
        for tmp in self.list:
            if tmp['name'] == teamName:
                return tmp['id']
        return -1

    def addTeam(self, teamName):
        if self.getTeam(teamName) == -1:
            print("Loading new team assets for team " + teamName + "...")
            tmp = {
                'name': teamName,
                'id': len(self.list),
                'sprites': self.createTeamSprites(len(self.list)),
            }
            self.list.append(tmp)
            print("Assets loaded with success")

    def getTeamSprites(self, teamName):
        for tmp in self.list:
            if tmp['name'] == teamName:
                return tmp['sprites']
        return 0

    def createTeamSprites(self, teamId):
        color = Color()
        teamYOffset = teamId * 3 * self.tileSize

        img_bas = self.spriteSheet.get_image(6 * self.tileSize, 0 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_haut = self.spriteSheet.get_image(2 * self.tileSize, 0 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_gauche = self.spriteSheet.get_image(4 * self.tileSize, 0 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_droite = self.spriteSheet.get_image(0 * self.tileSize, 0 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_take = self.spriteSheet.get_image(0 * self.tileSize, 1 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_layEgg = self.spriteSheet.get_image(2 * self.tileSize, 1 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_egg = self.spriteSheet.get_image(2 * self.tileSize, 2 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_hatch = self.spriteSheet.get_image(4 * self.tileSize, 1 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_incant = self.spriteSheet.get_image(6 * self.tileSize, 1 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_lvlUp = self.spriteSheet.get_image(0 * self.tileSize, 2 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)
        img_death = self.spriteSheet.get_image(1 * self.tileSize, 2 * self.tileSize + teamYOffset, self.tileSize, self.tileSize, color.WHITE)

        sprites = {
            'haut':     pygame.transform.scale(img_haut, self.tileDimension),
            'bas':      pygame.transform.scale(img_bas, self.tileDimension),
            'gauche':   pygame.transform.scale(img_gauche, self.tileDimension),
            'droite':   pygame.transform.scale(img_droite, self.tileDimension),
            'take':     pygame.transform.scale(img_take, self.tileDimension),
            'layEgg':   pygame.transform.scale(img_layEgg, self.tileDimension),
            'egg':      pygame.transform.scale(img_egg, self.tileDimension),
            'hatch':    pygame.transform.scale(img_hatch, self.tileDimension),
            'incant':   pygame.transform.scale(img_incant, self.tileDimension),
            'lvlUp':    pygame.transform.scale(img_lvlUp, self.tileDimension),
            'death':    pygame.transform.scale(img_death, self.tileDimension),
        }
        return sprites


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
        food = SpriteSheet("src/client/gui/assets/coeur.png")

        image_rubis_vert = rubis.get_image(167, 363, 30, 48, color.WHITE)
        image_rubis_bleu = rubis.get_image(195, 363, 30, 48, color.WHITE)
        image_rubis_jaune = rubis.get_image(223, 363, 30, 48, color.WHITE)
        image_rubis_rouge = rubis.get_image(251, 363, 30, 48, color.WHITE)
        image_rubis_violet = rubis.get_image(278, 363, 30, 48, color.WHITE)
        image_rubis_orange = rubis.get_image(305, 363, 30, 48, color.WHITE)
        image_coeur = food.get_image(0, 0, 48, 48, color.BLACK)

        self.rubis_vert = pygame.transform.scale(image_rubis_vert, (8, 16))
        self.rubis_bleu = pygame.transform.scale(image_rubis_bleu, (8, 16))
        self.rubis_jaune = pygame.transform.scale(image_rubis_jaune, (8, 16))
        self.rubis_rouge = pygame.transform.scale(image_rubis_rouge, (8, 16))
        self.rubis_violet = pygame.transform.scale(image_rubis_violet, (8, 16))
        self.rubis_orange = pygame.transform.scale(image_rubis_orange, (8, 16))
        self.food = pygame.transform.scale(image_coeur, (12, 12))

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

    def display_food(self, window, coordFood):
        if coordFood.nb_resource > 0:
            print("\n\n\nfood\n\n\n")
            window.blit(self.food, (coordFood.case_x, coordFood.case_y))


class CoordResource:
    def __init__(self, nb_resource, x, y):
        self.x = x
        self.y = y
        self.nb_resource = nb_resource
        self.case_x = random.randint(0, 32) + self.x * 48
        self.case_y = random.randint(0, 32) + self.y * 48

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
        GroundTexture = SpriteSheet("src/client/gui/assets/terrain1.png")
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
                    'thystame': coordResource,
                }
                self.map[y][x] = cell
        #print("onEggHatch egg_num={}".format(self.map))

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
        coordFood = CoordResource(resources['food'], x, y)
        self.map[y][x]['food'] = self.check_if_resource_exist(self.map[y][x]['food'], coordFood)

    def display_content(self, window):
        for i in range(self.height):
            for j in range(self.width):
                window.blit(self.map[i][j]['texture'], (j * 48, i * 48))
                self.resource.display_linemate(window, self.map[i][j]['linemate'])
                self.resource.display_deraumere(window, self.map[i][j]['deraumere'])
                self.resource.display_sibur(window, self.map[i][j]['sibur'])
                self.resource.display_mendiane(window, self.map[i][j]['mendiane'])
                self.resource.display_phiras(window, self.map[i][j]['phiras'])
                self.resource.display_thystame(window, self.map[i][j]['thystame'])
                self.resource.display_food(window, self.map[i][j]['food'])

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
            player.update_animation()

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
        self.spriteSheet = Teams.instance().getTeamSprites(team)
        self.action_previous = 0
        self.action = 0

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

        self.animation_timer = 10
        self.animation_delay = 10

    def assign_model(self):
        pass
        """
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
            self.action = self.spriteSheet['bas']
        elif orientation == 2:
            self.direction = self.droite
            self.action = self.spriteSheet['droite']
        elif orientation == 4:
            self.direction = self.gauche
            self.action = self.spriteSheet['gauche']
        elif orientation == 3:
            self.direction = self.haut
            self.action = self.spriteSheet['haut']

    def update_animation(self, window):
        self.animation_timer -= 1
        if self.animation_timer == 0:
            self.get_next_animation()
            self.animation_timer = self.animation_delay
        window.blit(self.action, (self.x, self.y))

    def get_next_animation(self):
        if self.action == 'haut':
            self.action = 'haut2'
        elif self.action == 'haut2':
            self.action = 'haut'
        elif self.action == 'bas':
            self.action = 'bas2'
        elif self.action == 'bas2':
            self.action = 'bas'
        elif self.action == 'droite':
            self.action = 'droite2'
        elif self.action == 'droite2':
            self.action = 'droite'
        elif self.action == 'gauche':
            self.action = 'gauche2'
        elif self.action == 'gauche2':
            self.action = 'gauche'
        elif self.action == 'take':
            self.action = 'take2'
        elif self.action == 'take2':
            self.action = 'take'
        elif self.action == 'layEgg':
            self.action = 'layEgg2'
        elif self.action == 'layEgg2':
            self.action = 'layEgg'
        elif self.action == 'egg':
            pass
        elif self.action == 'hatch':
            self.action = 'hatch2'
        elif self.action == 'hatch2':
            self.action = 'hatch'
        elif self.action == 'incant':
            pass
        elif self.action == 'lvlUp':
            pass
        elif self.action == 'death':
            pass