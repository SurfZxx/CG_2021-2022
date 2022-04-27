import OpenGL.GL as GL

from core.base import Base
from math import pi
from geometry import geometry
from core_ext.renderer import Renderer
from geometry.box import BoxGeometry
from geometry.cylindrical import CylindricalGeometry
from geometry.cuboid import CuboidGeometry
from geometry.cylinder import CylinderGeometry
from geometry.rectangle import RectangleGeometry
from geometry.polygon import PolygonGeometry
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from material.surface import SurfaceMaterial
from core.matrix import Matrix
from core.uniform import Uniform

class Example(Base) :
    def initialize(self):
        print ("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        geometry = CuboidGeometry()
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
        
        # movement speed, units per second
        # self.move_speed = 0.5
        # rotation speed, radians per second
        # self.turn_speed = 90 * (pi / 180)
        
        
    def update(self) :
        
        self.mesh.rotate_y(0.02514)
        self.mesh.rotate_x(0.01337)
        self.renderer.render(self.scene, self.camera)
        
        # move_amount = self.move_speed * self.delta_time
        # turn_amount = self.turn_speed * self.delta_time
        # # global translation
        # if self.input.is_key_pressed('w'):
        #     m = Matrix.make_translation(0, move_amount, 0)
        #     self.model_matrix.data = m @ self.model_matrix.data
        # if self.input.is_key_pressed('s'):
        #     m = Matrix.make_translation(0, -move_amount, 0)
        #     self.model_matrix.data = m @ self.model_matrix.data
        # if self.input.is_key_pressed('a'):
        #     m = Matrix.make_translation(-move_amount, 0, 0)
        #     self.model_matrix.data = m @ self.model_matrix.data
        # if self.input.is_key_pressed('d'):
        #     m = Matrix.make_translation(move_amount, 0, 0)
        #     self.model_matrix.data = m @ self.model_matrix.data
        
        
Example(screen_size=[800, 600]).run()