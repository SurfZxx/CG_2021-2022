"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class ChairObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():
        seat = BoxGeometry(width=1, height=0.1, depth=1)
        legs = BoxGeometry(width=0.1, height=0.1, depth=0.8)
        back = BoxGeometry(width=1.2, height=0.1, depth=1)

        #material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        #material = SurfaceMaterial(
        #    property_dict= {
        #        "useVertexColors": True,
        #        "wireframe": True,
        #        "lineWidth": 8
        #    }
        #)

        lightwood_texture = Texture(file_name="images/light-wood.jpg")
        lightwood_material = TextureMaterial(texture=lightwood_texture)

        darkbrownwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkbrownwood_material = TextureMaterial(texture=darkbrownwood_texture)

        wicker_texture = Texture(file_name="images/wicker_texture.jpg")
        wicker_material = TextureMaterial(texture=wicker_texture)



        mesh = Mesh(seat, darkbrownwood_material)
        mesh1 = Mesh(legs, darkbrownwood_material)
        mesh2 = Mesh(legs, darkbrownwood_material)
        mesh3 = Mesh(legs, darkbrownwood_material)
        mesh4 = Mesh(legs, darkbrownwood_material)
        mesh5 = Mesh(back, darkbrownwood_material)
    
        mesh.translate(0, 0, 0)
        mesh1.translate(-0.45, -0.4, -0.45)
        mesh1.rotate_x(1.57079)
        mesh2.translate(-0.45, -0.4, 0.45)
        mesh2.rotate_x(1.57079)
        mesh3.translate(0.45, -0.4, 0.45)
        mesh3.rotate_x(1.57079)
        mesh4.translate(0.45, -0.4, -0.45)
        mesh4.rotate_x(1.57079)
        mesh5.rotate_z(1.57079)
        mesh5.translate(0.55, 0.45, 0)


        mesh.add(mesh1)
        mesh.add(mesh2)
        mesh.add(mesh3)
        mesh.add(mesh4)
        mesh.add(mesh5)


        return mesh
