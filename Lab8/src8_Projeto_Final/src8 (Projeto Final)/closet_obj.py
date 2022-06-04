from core.base import Base
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry

class closetObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def getObj():

        geo_sides = BoxGeometry(width=0.10, height=2.5, depth=1)
        geo_base  = BoxGeometry(width=0.10, height=2, depth=1)
        geo_top   = BoxGeometry(width=0.10, height=2.2, depth=1.15)
        geo_knobs = SphereGeometry(radius=0.05, radius_segments=32, height_segments=16)

        # material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})

        material = SurfaceMaterial(property_dict={"useVertexColors": True})

        # material = SurfaceMaterial(
        #     property_dict= {
        #         "useVertexColors": True,
        #         "wireframe": True,
        #         "lineWidth": 8
        #     }
        # )


        lightwood_texture = Texture(file_name="images/light-wood.jpg")
        lightwood_material = TextureMaterial(texture=lightwood_texture)

        darkbrownwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkbrownwood_material = TextureMaterial(texture=darkbrownwood_texture)

        metal_texture = Texture(file_name="images/metal.jpg")
        metal_material = TextureMaterial(texture=metal_texture)

        meshMaster = Mesh(geo_sides, darkbrownwood_material)
        meshMaster.rotate_y(1.57079632679)

        mesh1 = Mesh(geo_sides, darkbrownwood_material)
        mesh2 = Mesh(geo_sides, darkbrownwood_material)
        mesh3 = Mesh(geo_sides, darkbrownwood_material)
        mesh4 = Mesh(geo_sides, lightwood_material)
        mesh5 = Mesh(geo_sides, lightwood_material)
        mesh6 = Mesh(geo_base , darkbrownwood_material)
        mesh7 = Mesh(geo_top  , darkbrownwood_material)
        mesh8 = Mesh(geo_knobs, metal_material)
        mesh9 = Mesh(geo_knobs, metal_material)

        mesh1.translate(0,0,-1)

        mesh2.rotate_y(-1.57079632679)
        mesh2.translate(0.45,0,0.45)

        mesh3.rotate_y(-1.57079632679)
        mesh3.translate(-1.45,0,0.45)

        mesh4.translate(-1,0,0)

        mesh5.translate(-1,0,-1)

        mesh6.rotate_z(1.57079632679)
        mesh6.rotate_x(1.57079632679)
        mesh6.translate(-1.20,-0.5,-0.5)
        
        mesh7.rotate_z(1.57079632679)
        mesh7.rotate_x(1.57079632679)
        mesh7.translate(1.21,-0.5,-0.5)

        mesh8.translate(-1.09,0,-0.25)

        mesh9.translate(-1.09,0,-0.75)
        
        meshMaster.add(mesh1)
        meshMaster.add(mesh2)
        meshMaster.add(mesh3)
        meshMaster.add(mesh4)
        meshMaster.add(mesh5)
        meshMaster.add(mesh6)
        meshMaster.add(mesh7)
        meshMaster.add(mesh8)
        meshMaster.add(mesh9)

        # meshMaster.translate(0,0.25,0)

        return(meshMaster)