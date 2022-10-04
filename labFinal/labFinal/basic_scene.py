import re
import numpy as np
import math
import pathlib
import sys
import random

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from desk_obj import DeskObject
from closet_obj import closetObject
from chair_obj import ChairObject
from bedsidetable_obj import BedsideTObject

from spider_obj import spiderObject
from spider1_obj import spider1Object
from spider2_obj import spider2Object
from spider3_obj import spider3Object

from box_obj import boxObject
from bed_obj import bedObject
from tv_obj import tvObject
from couch_obj import CouchObject
from poster import posterObject
from door_obj import doorObject
from carpet_obj import CarpetObject
from battle_background import battleBackground
from fire_element_obj import fireObject
from water_element_obj import waterObject
from grass_element_obj import grassObject
from fire_element_obj_h import fireObject_h
from water_element_obj_h import waterObject_h
from grass_element_obj_h import grassObject_h
from geometry.rectangle import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.box import BoxGeometry
from extras.movement_rig import MovementRig
from core_ext.texture import Texture
from material.texture import TextureMaterial

from leave_txt import leaveObject
from win_txt import winObject
from lose_txt import loseObject

import time

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add box movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        # 0.18, -3, 5
        self.rig.set_position([-7.25, 4.75, 4.75])
        # self.rig.set_position([5, 2, -3.8])

        # self.camera.rotate_y(1.57079632679)

        # self.rig.set_position([0, -10, -4])            #battle view
        bedroom_geometry = BoxGeometry(width=15, height=10, depth=10)
        bedroom_material = TextureMaterial(texture=Texture(file_name="images/wall_texture.jpg"))
        bedroom = Mesh(bedroom_geometry, bedroom_material)
        self.scene.add(bedroom)
        floor_geometry = RectangleGeometry(width=20, height=20)
        floor_material = TextureMaterial(
            texture=Texture(file_name="images/floor_texture.jpg"),
            property_dict={"repeatUV": [20, 20]}
        )
        grass = Mesh(floor_geometry, floor_material)
        grass.rotate_x(-math.pi/2)
        self.scene.add(grass)

        self.desk = DeskObject.initialize()
        self.desk.translate(-4.6, 1.7, -4)
        self.desk.scale(1.7)

        self.closet = closetObject.initialize()
        self.closet.translate(1.05, -6.5, 3.1)
        self.closet.rotate_x(-1.57079632679)
        self.closet.scale(1.75)

        self.chair = ChairObject.initialize()
        self.chair.translate(-3.5, 1, -3.2)
        self.chair.rotate_y(1.57079632679)
        self.chair.scale(1.2)

        self.bedsidetable = BedsideTObject.initialize()
        self.bedsidetable.translate(4.2, -1.8, -1.5)
        self.bedsidetable.rotate_z(1.57079632679)
        self.bedsidetable.rotate_x(-1.57079632679)
        self.bedsidetable.scale(1.5)

        self.box = boxObject.initialize()
        self.box.translate(0, 1.1, -4.9)
        self.box.scale(1.2)

        self.bed = bedObject.initialize()
        self.bed.translate(-0.7, 0.5, 1.8)
        self.bed.rotate_y(1.57079632679)
        self.bed.scale(2)

        self.tv = tvObject.initialize()
        self.tv.translate(4.25, 2.6, -5.75)
        self.tv.rotate_y(0.1963495408)
        self.tv.scale(1)

        self.couch = CouchObject.initialize()
        self.couch.translate(-5.5, 1, 3.85)
        self.couch.rotate_y(3.14159265359)
        self.couch.scale(1.4)

        self.poster = posterObject.initialize()
        self.poster.translate(0, 3, -5)
        self.poster.rotate_y(-1.57079632679)
        self.poster.scale(2)

        self.door = doorObject.initialize()
        self.door.translate(7.475, 2, -2.5)
        self.door.scale(1.5)

        self.carpet = CarpetObject.initialize()
        self.carpet.translate(2.5, 0.01, 0.5)
        self.carpet.rotate_x(1.57079632679)
        self.carpet.rotate_z(1.57079632679)

        self.battlebackground = battleBackground.initialize()
        self.battlebackground.translate(0, -10, -10)

        self.fire_el = fireObject.initialize()
        self.fire_el.translate(-1.5, -8.5, -9.9)

        self.water_el = waterObject.initialize()
        self.water_el.translate(-1.5, -10, -9.9)

        self.grass_el = grassObject.initialize()
        self.grass_el.translate(-1.5, -11.5, -9.9)

        self.fire_el_hostile = fireObject_h.initialize()
        self.fire_el_hostile.translate(1.5, -8.5, -10.1)

        self.water_el_hostile = waterObject_h.initialize()
        self.water_el_hostile.translate(1.5, -10, -10.1)

        self.grass_el_hostile = grassObject_h.initialize()
        self.grass_el_hostile.translate(1.5, -11.5, -10.1)

        self.spiderbattle1 = spiderObject.initialize()
        self.spiderbattle1.translate(-10, -9.75, -3.5)
        self.spiderbattle1.rotate_z(-1.57079632679)
        self.spiderbattle1.rotate_x(1.57079632679)
        self.spiderbattle1.rotate_y(3.14159265359)
        self.spiderbattle1.scale(0.7)

        self.spiderbattle2 = spiderObject.initialize()
        self.spiderbattle2.translate(-10, -9.75, 3.5)
        self.spiderbattle2.rotate_z(-1.57079632679)
        self.spiderbattle2.rotate_x(-1.57079632679)
        self.spiderbattle2.rotate_y(3.14159265359)
        self.spiderbattle2.scale(0.7)

        self.spider = spiderObject.initialize()
        self.spider.translate(0.18, -3, 5)
        self.spider.rotate_x(-1.57079632679)
        self.spider.scale(0.6)

        self.hostile1 = spider1Object.initialize()
        self.hostile1.translate(0.18, 4.4, 3.4)
        self.hostile1.rotate_x(3.14159265359)
        self.hostile1.scale(0.6)

        self.hostile2 = spider2Object.initialize()
        self.hostile2.translate(0.18, -2.5, -6.9)
        self.hostile2.rotate_x(1.57079632679)
        self.hostile2.scale(0.6)

        self.hostile3 = spider3Object.initialize()
        self.hostile3.translate(0.18, 4.2, -3.1)
        self.hostile3.rotate_x(3.14159265359)
        self.hostile3.scale(0.6)

        self.leavebattle = leaveObject.initialize()
        self.leavebattle.translate(3.5, -8, -10.1)

        self.wintxt = winObject.initialize()
        self.wintxt.translate(0, -8, -10.1)

        self.losetxt = loseObject.initialize()
        self.losetxt.translate(0, -8, -10.1)

        #Terrain 1
        self.scene.add(self.desk)
        self.scene.add(self.closet)
        self.scene.add(self.chair)
        self.scene.add(self.bedsidetable)
        self.scene.add(self.spider)
        self.scene.add(self.box)
        self.scene.add(self.bed)
        self.scene.add(self.tv)
        self.scene.add(self.couch)
        self.scene.add(self.poster)
        self.scene.add(self.door)
        self.scene.add(self.carpet)
        self.scene.add(self.hostile1)
        self.scene.add(self.hostile2)
        self.scene.add(self.hostile3)

        #Terrain 2
        self.scene.add(self.battlebackground)
        self.scene.add(self.spiderbattle1)
        self.scene.add(self.spiderbattle2)
        self.scene.add(self.fire_el)
        self.scene.add(self.water_el)
        self.scene.add(self.grass_el)
        self.scene.add(self.fire_el_hostile)
        self.scene.add(self.water_el_hostile)
        self.scene.add(self.grass_el_hostile)
        self.scene.add(self.leavebattle)
        self.scene.add(self.wintxt)
        self.scene.add(self.losetxt)

        self.setSpiderCoordinates()
        self.hostile = 0

        self.score = 0
        self.resetBattleScore()

        self.i = 0.1
        self.leaveBattleVar = 0

    def resetTexts(self):
        self.wintxt.set_position([0, -7.3, -10.1])
        self.losetxt.set_position([0, -7.3, -10.1])
        self.leavebattle.set_position([3.5, -12.7, -10.1])

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)

        if self.terrains() == 1:
            if self.input.is_key_pressed("p"):
                if self.hostiles():
                    self.terrain = 2
                    self.rig.set_position([0, -10, -4])
                    print("wins: " + format(self.victories))
                    print("draws: " + format(self.draws))
                    print("losses: " + format(self.losses))
                    self.resetElements() 
                    
            if self.input.is_key_pressed("down"):
                self.spiderX += -self.i
                if self.checkCollisionObjects() == False:
                    self.spider.translate(0, -self.i, 0)
                    # self.rig.set_position([-7.25, 4.75-self.i, 4.75])
                else:
                    self.spiderX += self.i
                print("x=" + format(self.spiderX))

            if self.input.is_key_pressed("up"):
                self.spiderX += self.i
                if self.checkCollisionObjects() == False:
                    self.spider.translate(0, self.i, 0)
                    # self.rig.set_position([-7.25, 4.75+self.i, 4.75])
                else:
                    self.spiderX += -self.i
                print("x=" + format(self.spiderX))

            if self.input.is_key_pressed("right"):
                self.spiderY += -self.i
                if self.checkCollisionObjects() == False:
                    self.spider.translate(0, 0, -self.i)
                    # self.rig.set_position([-7.25, 4.75, 4.75-self.i])
                else:
                    self.spiderY += self.i
                print("y=" + format(self.spiderY))

            if self.input.is_key_pressed("left"):
                self.spiderY += self.i
                if self.checkCollisionObjects() == False:
                    self.spider.translate(0, 0, self.i)
                    # self.rig.set_position([-7.25, 4.75, 4.75+self.i])
                else:
                    self.spiderY += -self.i
                print("y=" + format(self.spiderY))

            

        else:
            if self.input.is_key_pressed("j"): 
                self.player = 0 # Fire
                self.water_el.set_position([-1.5, -10, -10.1])
                self.grass_el.set_position([-1.5, -11.5, -10.1])
                self.fire_el.set_position([-1.5, -8.5, -9.9])
                self.elementGame()
            if self.input.is_key_pressed("k"):
                self.player = 1 # Water
                self.fire_el.set_position([-1.5, -8.5, -10.1])
                self.grass_el.set_position([-1.5, -11.5, -10.1])
                self.water_el.set_position([-1.5, -10, -9.9])
                self.elementGame()
            if self.input.is_key_pressed("l"):
                self.player = 2 # Grass
                self.fire_el.set_position([-1.5, -8.5, -10.1])
                self.water_el.set_position([-1.5, -10, -10.1])
                self.grass_el.set_position([-1.5, -11.5, -9.9])
                self.elementGame()

            if self.leaveBattleVar == 1 and self.input.is_key_pressed("m"):
                self.resetTerrain()
                self.resetBattleScore() 
                self.updateScore()
                self.resetHostiles()
                self.rig.set_position([-7.25, 4.75, 4.75])
                self.resetTexts()

    def resetElements(self):
        self.fire_el.set_position([-1.5, -8.5, -9.9])
        self.water_el.set_position([-1.5, -10, -9.9])
        self.grass_el.set_position([-1.5, -11.5, -9.9])

        self.fire_el_hostile.set_position([1.5, -8.5, -10.1])
        self.water_el_hostile.set_position([1.5, -10, -10.1])
        self.grass_el_hostile.set_position([1.5, -11.5, -10.1])

    def updateScore(self):
        self.score += 1

    def resetBattleScore(self):
        self.victories = 0
        self.losses = 0
        self.draws = 0

    def result(self):
        if  self.victories == 3:
            print("You won the battle")
            self.leaveBattleVar = 1
            self.wintxt.set_position([0, -7.3, -9.9])
            self.losetxt.set_position([0, -7.3, -10.1])
            self.leavebattle.set_position([3.5, -12.7, -9.9])
            print("Your Score = " + format(self.score))
            print("To leave press 'm'")

        if  self.losses == 3:
            print("You lost the battle")
            self.leaveBattleVar = 1
            self.losetxt.set_position([0, -7.3, -9.9])
            self.wintxt.set_position([0, -7.3, -10.1])
            self.leavebattle.set_position([3.5, -12.7, -9.9])
            print("Your Score = " + format(self.score))
            print("To leave press 'm'")

    def elementGame(self):   
        self.opponent = random.randint(0, 2)
        # print(format(self.opponent))

        if self.opponent == 0:
            self.fire_el_hostile.set_position([1.5, -8.5, -9.9])
            self.water_el_hostile.set_position([1.5, -10, -10.1])
            self.grass_el_hostile.set_position([1.5, -11.5, -10.1])
        if self.opponent == 1:
            self.water_el_hostile.set_position([1.5, -10, -9.9])
            self.fire_el_hostile.set_position([1.5, -8, -10.1])
            self.grass_el_hostile.set_position([1.5, -11.5, -10.1])
        if self.opponent == 2:
            self.grass_el_hostile.set_position([1.5, -11.5, -9.9])
            self.water_el_hostile.set_position([1.5, -10, -10.1])
            self.fire_el_hostile.set_position([1.5, -8, -10.1])

        self.elementOrder()
        self.result()

        time.sleep(1)

    # 0 = Fire
    # 1 = Water
    # 2 = Grass
    
    # 0 wins over 2
    # 1 wins over 0
    # 2 wins over 1

    def elementOrder(self):
        if self.opponent == 0 and self.player == 2:
            self.losses += 1
        if self.opponent == 1 and self.player == 0:
            self.losses += 1
        if self.opponent == 2 and self.player == 1:
            self.losses += 1
        if self.opponent == self.player:
            self.draws += 1

        if self.opponent == 0 and self.player == 1:
            self.victories += 1
        if self.opponent == 1 and self.player == 2:
            self.victories += 1
        if self.opponent == 2 and self.player == 0:
            self.victories += 1

        print("wins: " + format(self.victories))
        print("draws: " + format(self.draws))
        print("losses: " + format(self.losses))

    def resetTerrain(self):
        self.terrain = 1

    def resetHostiles(self):
        self.hostile = 0

    def terrains(self):
        if self.hostile != 0:
            # self.rig.set_position([0, -10, -4])
            return 2
        # self.rig.set_position([-7.25, 4.75, 4.75])
        return 1

    def setSpiderCoordinates(self):
        self.spiderX = 0.18
        self.spiderY = -3
        self.spiderZ = 5

    def hostiles(self):

        #hostile 1
        if self.spiderX > 0.98  and self.spiderX < 3.4 and self.spiderY > 6.5 and self.spiderY < 7.5:
            self.hostile = 1
            return True

        #hostile 2
        if self.spiderX > 17.26  and self.spiderX < 18.26 and self.spiderY < -0.3:
            self.hostile = 2
            return True

        #hostile 3
        if self.spiderX > 13.18 and self.spiderX < 14.15 and self.spiderY > 6 and self.spiderY < 8:
            self.hostile = 3
            return True
    
        return False

    def checkCollisionRoom(self):
        if self.spiderX < -3.2 or self.spiderX > 20.16 or self.spiderY > 9.4 or self.spiderY < -5.4:
            return True
        return False

    def checkCollisionObjects(self): #return True if collision or False if no collision
        
        #room walls
        if self.checkCollisionRoom():
            return True

        #closet
        if self.spiderX < 0 and self.spiderY > 3.2:
            return True

        #bed side table
        if self.spiderX > 3.4 and self.spiderX < 6.15 and self.spiderY > 6.8:
            return True

        #bed
        if self.spiderX > 6.15 and self.spiderX < 13.18 and self.spiderY > -0.55:
            return True
        
        #couch
        if self.spiderX > 14.15 and self.spiderY > 5.7:
            return True

        #chest
        if self.spiderX > 5.15 and self.spiderX < 11.8 and self.spiderY < -3.2:
            return True
        
        #table
        if self.spiderX > 11 and self.spiderX < 20.16 and self.spiderY < -2.3 :
            return True

        #chair
        if self.spiderX > 12.55 and self.spiderX < 16.15 and self.spiderY < -1.4:
            return True

        #spider1
        if self.spiderX > 0.98  and self.spiderX < 3.4 and self.spiderY > 7.5:
            return True

        #spider2
        if self.spiderX > 18.26 and self.spiderX < 20.16 and self.spiderY < -0.3:
            return True

        #spider3
        if self.spiderX > 13.18 and self.spiderX < 14.15 and self.spiderY > 7:
            return True

        return False

# Instantiate this class and run the program
Example(screen_size=[950, 750]).run()