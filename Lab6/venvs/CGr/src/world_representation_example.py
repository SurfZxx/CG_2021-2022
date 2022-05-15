import numpy as np
import math
import pathlib
import sys
import pywavefront

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from material.surface import SurfaceMaterial
from geometry.box import BoxGeometry
from core.obj_reader import my_obj_reader
from core.utils import Utils
from core.uniform import Uniform
from core.attribute import Attribute


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")       
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        # self.camera.set_position([0.5, 1, 5])
        # geometry = pywavefront.Wavefront('closet.obj', collect_faces=True)
        #apagar
        
        # vs_code = """
        #     in vec3 position;
        #     uniform mat4 projectionMatrix;
        #     uniform mat4 modelMatrix;
        #     void main()
        #     {
        #         gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
        #     }
        # """
        # fs_code = """
        #     in vec3 color;
        #     out vec4 fragColor;
        #     void main()
        #     {
        #         fragColor = vec4(1.0, 1.0, 1.0, 1.0);
        #     }
        # """
        # self.program_ref = Utils.initialize_program(vs_code, fs_code)
        
        # position_data = my_obj_reader('core/Bed6Main.obj')
        # self.vertex_count = len(position_data)
        # position_attribute = Attribute('vec3', position_data)
        # position_attribute.associate_variable(self.program_ref, 'position')
        
        
        
        
        #apagar
        # geometry = position_data
        geometry = BoxGeometry()
        
        
        
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        self.mesh = Mesh(geometry, material)
        self.rig = MovementRig()
        self.rig.add(self.mesh)
        self.rig.add(self.camera)
        self.rig.set_position([0.5, 1, 5])
        self.scene.add(self.rig)
        #axes = AxesHelper(axis_length=2)
        #self.scene.add(axes)
        grid = GridHelper(
            size=20,
            grid_color=[1, 1, 1],
            center_color=[1, 1, 0]
        )
        grid.rotate_x(-math.pi / 2)
        # self.scene.add(grid)
        # self.scene.add(geometry)
        self.scene.add(self.mesh)
        

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
        
        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()