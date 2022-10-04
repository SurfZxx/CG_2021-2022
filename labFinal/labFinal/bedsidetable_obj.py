"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class BedsideTObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():
        topTable = BoxGeometry(width=1.1, height=0.1, depth=1)
        sideTable = BoxGeometry(width=1, height=0.1, depth=1)
        shelfs = BoxGeometry(width=1.05, height=0.025, depth=1)
        doorshelfs = BoxGeometry(width=1, height=0.025, depth=0.475)
        knobshelf = SphereGeometry(radius= 0.05, radius_segments= 32, height_segments= 16)
        backtable = BoxGeometry(width=1, height=0.025, depth=1)

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

        metal_texture = Texture(file_name="images/metal.jpg")
        metal_material = TextureMaterial(texture=metal_texture)

        mesh = Mesh(topTable, darkbrownwood_material)
        mesh1 = Mesh(sideTable, darkbrownwood_material)
        mesh2 = Mesh(sideTable, darkbrownwood_material)
        mesh3 = Mesh(shelfs, darkbrownwood_material)
        mesh4 = Mesh(shelfs, darkbrownwood_material)
        mesh5 = Mesh(doorshelfs, lightwood_material)
        mesh6 = Mesh(doorshelfs, lightwood_material)
        mesh7 = Mesh(knobshelf, metal_material)
        mesh8 = Mesh(knobshelf, metal_material)
        mesh9 = Mesh(backtable, darkbrownwood_material)
    
        
        mesh.rotate_x(1.57079)
        mesh.rotate_z(1.57079)
        mesh.translate(0, 0, 0)
        mesh1.rotate_x(1.57079)
        mesh1.rotate_z(1.57079)
        mesh1.translate(0, 0.5, 0.5)
        mesh2.rotate_x(1.57079)
        mesh2.rotate_z(1.57079)
        mesh2.translate(0, -0.5, 0.5)
        mesh3.translate(0, -0.5, 0)
        mesh4.translate(0, -0.985, 0)
        mesh5.translate(0, -0.275, 0.475)
        mesh5.rotate_x(1.57079)
        mesh6.translate(0, -0.75, 0.475)
        mesh6.rotate_x(1.57079)
        mesh7.translate(0.3, -0.75, 0.525)
        mesh8.translate(0, -0.275, 0.525)
        mesh9.translate(0, -0.5, -0.475)
        mesh9.rotate_x(1.57079)

        mesh.add(mesh1)
        mesh.add(mesh2)
        mesh.add(mesh3)
        mesh.add(mesh4)
        mesh.add(mesh5)
        mesh.add(mesh6)
        mesh.add(mesh7)
        mesh.add(mesh8)
        mesh.add(mesh9)

        return mesh