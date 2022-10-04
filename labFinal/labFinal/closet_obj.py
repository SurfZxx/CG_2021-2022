"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry

class closetObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():

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


        lightWood_texture = Texture(file_name="images/light-wood.jpg")
        lightWood_material = TextureMaterial(texture=lightWood_texture)

        metal_texture = Texture(file_name="images/metal.jpg")
        metal_material = TextureMaterial(texture=metal_texture)

        darkBrown_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkBrown_material = TextureMaterial(texture=darkBrown_texture)

        meshMaster = Mesh(geo_base, darkBrown_material) # Base
        meshMaster.rotate_z(1.57079632679)
        meshMaster.translate(-1,0,0)
        
        mesh1 = Mesh(geo_sides, darkBrown_material) # Left side
        mesh2 = Mesh(geo_sides, darkBrown_material) # Right side
        mesh3 = Mesh(geo_sides, darkBrown_material) # Back left
        mesh4 = Mesh(geo_sides, darkBrown_material) # Back right
        mesh5 = Mesh(geo_sides, lightWood_material) # Front left
        mesh6 = Mesh(geo_sides, lightWood_material) # Front right
        mesh7 = Mesh(geo_top  , darkBrown_material) # Top side
        mesh8 = Mesh(geo_knobs, metal_material) # Left knob
        mesh9 = Mesh(geo_knobs, metal_material) # Right knob

        mesh1.translate(1.2,1,0)
        mesh1.rotate_z(1.57079632679)

        mesh2.translate(1.2,-1,0)
        mesh2.rotate_z(1.57079632679)

        mesh3.rotate_z(1.57079632679)
        mesh3.rotate_y(1.57079632679)
        mesh3.translate(0.45,-1.2,0.5)

        mesh4.rotate_z(1.57079632679)
        mesh4.rotate_y(1.57079632679)
        mesh4.translate(0.45,-1.2,-0.5)

        mesh5.rotate_z(1.57079632679)
        mesh5.rotate_y(1.57079632679)
        mesh5.translate(-0.45,-1.2,0.5)

        mesh6.rotate_z(1.57079632679)
        mesh6.rotate_y(1.57079632679)
        mesh6.translate(-0.45,-1.2,-0.5)

        mesh7.translate(2.45,0,0)

        mesh8.translate(1,0.2,0.55)

        mesh9.translate(1,-0.2,0.55)
        
        meshMaster.add(mesh1) 
        meshMaster.add(mesh2)
        meshMaster.add(mesh3)
        meshMaster.add(mesh4)
        meshMaster.add(mesh5)
        meshMaster.add(mesh6)
        meshMaster.add(mesh7)
        meshMaster.add(mesh8)
        meshMaster.add(mesh9)



        return(meshMaster)