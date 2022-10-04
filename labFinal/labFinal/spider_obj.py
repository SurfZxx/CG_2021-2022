"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry

class spiderObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():

        body = BoxGeometry(width=0.30, height=1, depth=0.4)
        leg  = BoxGeometry(width=0.10, height=1, depth=0.1)
        head = BoxGeometry(width=0.5, height=0.5, depth=0.5)
        back = BoxGeometry(width=0.5, height=0.7, depth=0.5)

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

        spider_texture = Texture(file_name="images/spider.jpg")
        spider_material = TextureMaterial(texture=spider_texture)

        meshMaster = Mesh(body, spider_material) # body
        meshMaster.rotate_x(1.57079632679)
        meshMaster.rotate_y(1.57079632679)

        mesh1 = Mesh(head, spider_material) # Head
        mesh2 = Mesh(back, spider_material) # back
        mesh3 = Mesh(leg, spider_material)  # leg 1 right
        mesh4 = Mesh(leg, spider_material)  # leg 2 right
        mesh5 = Mesh(leg, spider_material)  # leg 3 right
        mesh6 = Mesh(leg, spider_material)  # leg 4 right
        mesh7 = Mesh(leg, spider_material)  # leg 1 left
        mesh8 = Mesh(leg, spider_material)  # leg 2 left
        mesh9 = Mesh(leg, spider_material)  # leg 3 left
        mesh10 = Mesh(leg, spider_material) # leg 4 left

        mesh1.translate(0,0.6,0)
        mesh2.translate(0,-0.4,0)
        #===================================================
        mesh3.rotate_x(1.57079632679)
        mesh3.translate(-0.1,0.4,0)
        mesh3.rotate_x(0.5)
        mesh3.rotate_z(0.3)

        mesh4.rotate_x(1.57079632679)
        mesh4.translate(-0.1,0.4,-0.1)
        mesh4.rotate_x(0.3)
        mesh4.rotate_z(0.3)

        mesh5.rotate_x(1.57079632679)
        mesh5.translate(-0.1,0.4,-0.2)
        mesh5.rotate_x(0.1)
        mesh5.rotate_z(0.3)

        mesh6.rotate_x(1.57079632679)
        mesh6.translate(-0.1,0.4,-0.3)
        mesh6.rotate_x(-0.1)
        mesh6.rotate_z(0.3)
        #===================================================
        mesh7.rotate_x(-1.57079632679)
        mesh7.translate(-0.1,0.4,0)
        mesh7.rotate_x(-0.5)
        mesh7.rotate_z(0.3)

        mesh8.rotate_x(-1.57079632679)
        mesh8.translate(-0.1,0.4,0.1)
        mesh8.rotate_x(-0.3)
        mesh8.rotate_z(0.3)

        mesh9.rotate_x(-1.57079632679)
        mesh9.translate(-0.1,0.4,0.2)
        mesh9.rotate_x(-0.1)
        mesh9.rotate_z(0.3)

        mesh10.rotate_x(-1.57079632679)
        mesh10.translate(-0.1,0.4,0.3)
        mesh10.rotate_x(0.1)
        mesh10.rotate_z(0.3)
        
        meshMaster.add(mesh1) 
        meshMaster.add(mesh2)
        meshMaster.add(mesh3)
        meshMaster.add(mesh4)
        meshMaster.add(mesh5)
        meshMaster.add(mesh6)
        meshMaster.add(mesh7)

        meshMaster.add(mesh8)
        meshMaster.add(mesh9)
        meshMaster.add(mesh10)

        return(meshMaster)