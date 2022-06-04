"""An example of a basic scene: spinning cube"""


from core.base import Base
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.movement_rig import MovementRig
from core_ext.renderer import Renderer
from core_ext.scene import Scene

class MonaBox(Base):
    def getObj():
        backside = BoxGeometry(width=2.5, height=1.0, depth=0.05)
        frontside = BoxGeometry(width=2.5, height=1.02, depth=0.05)
        downside = BoxGeometry(width=2.5, height=1.0, depth=0.05)
        upside = BoxGeometry(width=1, height=2.5, depth=0.05)
        boxside = BoxGeometry(width=1, height=0.05, depth=1)
        boxside1 = BoxGeometry(width=1, height=0.05, depth=1)

        # every_texture = Texture(file_name="images/everything.jpeg")
        # every_meterial = TextureMaterial(texture=every_texture)
        
        lightwood_texture = Texture(file_name="images/light-wood.jpg")
        lightwood_material = TextureMaterial(texture=lightwood_texture)

        darkwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkwood_material = TextureMaterial(texture=darkwood_texture)

  

        material = SurfaceMaterial(property_dict={"useVertexColors": True})
     

        mesh00 = Mesh(backside, darkwood_material)
        mesh11 = Mesh(downside, darkwood_material)
        mesh22 = Mesh(frontside, lightwood_material)
        mesh33 = Mesh(boxside, darkwood_material)
        mesh44 = Mesh(boxside1, darkwood_material)
        mesh55 = Mesh(upside,  darkwood_material)
   
        mesh00.translate(0, -0.48, 0)
        mesh11.translate(0.0, -0.5, 0.48)
        mesh11.rotate_x(1.57079)
        mesh22.translate(0.0, -0.02, 1.0)
        mesh33.rotate_x(1.57079)
        mesh33.rotate_z(1.57079)
        mesh33.translate(0.5, -1.22, 0.0)
        mesh44.rotate_x(1.57079)
        mesh44.rotate_z(1.57079)
        mesh44.translate(0.5, 1.22, 0.0)
        mesh55.rotate_x(1.57079)
        mesh55.rotate_z(1.57079)
        mesh55.rotate_y(0.5)
        mesh55.translate(0.75, 0.0, -0.45)


        mesh00.add(mesh11)
        mesh00.add(mesh22)
        mesh00.add(mesh33)
        mesh00.add(mesh44)
        mesh00.add(mesh55)


        return mesh00
