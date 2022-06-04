import numpy as np
import math
import pathlib
import sys

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
from monasproject import MonaBox
from bed_obj import bedObject
from geometry.rectangle import RectangleGeometry
from geometry.sphere import SphereGeometry
from geometry.box import BoxGeometry
from extras.movement_rig import MovementRig
from core_ext.texture import Texture
from material.texture import TextureMaterial


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
        self.rig.set_position([0, 1, 4])
        bedroom_geometry = BoxGeometry(width=15, height=10, depth=15)
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

        self.desk = DeskObject.getObj()
        self.desk.translate(0, 1.2, 0)
        self.desk.scale(1.2)

        self.closet = closetObject.getObj()
        self.closet.translate(0, 1.25, 4)

        self.chair = ChairObject.getObj()
        self.chair.translate(0.5, 0.667, 0.5)
        self.chair.rotate_y(1.57079632679)
        self.chair.scale(0.8)

        self.bedsidetable = BedsideTObject.getObj()
        self.bedsidetable.translate(0, 3.5, -1)
        self.bedsidetable.rotate_z(-1.57079632679)
        self.bedsidetable.rotate_x(-1.57079632679)
        self.chair.scale(1.1)

        self.spider = spiderObject.getObj()
        self.spider.translate(0.25, 2, 0)
        self.spider.rotate_x(3.141592653589)
        self.spider.scale(0.8)

        self.monabox = MonaBox.getObj()
        self.monabox.translate(0, 1.1, -4)

        self.bed = bedObject.getObj()
        self.bed.translate(-4, 0.3, -4)
        self.bed.scale(1.2)

        self.scene.add(self.desk)
        self.scene.add(self.closet)
        self.scene.add(self.chair)
        self.scene.add(self.bedsidetable)
        self.scene.add(self.spider)
        self.scene.add(self.monabox)
        self.scene.add(self.bed)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)

        if self.input.is_key_pressed("up"):
            self.spider.translate(0, 0.1, 0)
        if self.input.is_key_pressed("down"):
            self.spider.translate(0, -0.1, 0)
        if self.input.is_key_pressed("left"):
            self.spider.translate(0, 0, 0.1)
        if self.input.is_key_pressed("right"):
            self.spider.translate(0, 0, -0.1)


# Instantiate this class and run the program
Example(screen_size=[950, 750]).run()