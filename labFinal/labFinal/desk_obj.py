
from core.base import Base
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class DeskObject(Base):
    def initialize():
        upperTable = BoxGeometry(width=3.15, height=0.1, depth=1.1)
        backTable = BoxGeometry(width=3, height=0.1, depth=1)
        lowerTable = BoxGeometry(width=1.8, height=0.05, depth=1)
        sideTable = BoxGeometry(width=1, height=0.1, depth=1)
        shelfs = BoxGeometry(width=1.05, height=0.025, depth=1)
        doorshelfs = BoxGeometry(width=1, height=0.025, depth=0.475)
        knobshelf = SphereGeometry(radius= 0.05, radius_segments= 32, height_segments= 16)

        lightwood_texture = Texture(file_name="images/light-wood.jpg")
        lightwood_material = TextureMaterial(texture=lightwood_texture)

        darkwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkwood_material = TextureMaterial(texture=darkwood_texture)

        metal_texture = Texture(file_name="images/metal.jpg")
        metal_material = TextureMaterial(texture=metal_texture)


        #material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        #material = SurfaceMaterial(
        #    property_dict= {
        #        "useVertexColors": True,
        #        "wireframe": True,
        #        "lineWidth": 8
        #    }
        #)

        mesh = Mesh(upperTable, darkwood_material)
        mesh1 = Mesh(backTable, darkwood_material)
        mesh2 = Mesh(lowerTable, lightwood_material)
        mesh3 = Mesh(sideTable, darkwood_material)
        mesh4 = Mesh(sideTable, darkwood_material)
        mesh5 = Mesh(sideTable, darkwood_material)
        mesh6 = Mesh(shelfs, darkwood_material)
        mesh7 = Mesh(shelfs, darkwood_material)
        mesh8 = Mesh(doorshelfs, lightwood_material)
        mesh9 = Mesh(doorshelfs, lightwood_material)
        mesh10 = Mesh(knobshelf, metal_material)
        mesh11 = Mesh(knobshelf, metal_material)
    
        mesh.translate(0, 0, 0)
        mesh1.translate(0, -0.5, -0.5)
        mesh1.rotate_x(1.57079)
        mesh2.translate(0.55, -0.225, 0)
        mesh3.rotate_x(1.57079)
        mesh3.rotate_z(1.57079)
        mesh3.translate(0, -1.5, 0.5)
        mesh4.rotate_x(1.57079)
        mesh4.rotate_z(1.57079)
        mesh4.translate(0, 0.4, 0.5)
        mesh5.rotate_x(1.57079)
        mesh5.rotate_z(1.57079)
        mesh5.translate(0, 1.5, 0.5)
        mesh6.translate(-0.95, -0.5, 0)
        mesh7.translate(-0.95, -0.985, 0)
        mesh8.translate(-0.95, -0.275, 0.475)
        mesh8.rotate_x(1.57079)
        mesh9.translate(-0.95, -0.75, 0.475)
        mesh9.rotate_x(1.57079)
        mesh10.translate(-0.6, -0.75, 0.525)
        mesh11.translate(-0.95, -0.275, 0.525)

        mesh.add(mesh1)
        mesh.add(mesh2)
        mesh.add(mesh3)
        mesh.add(mesh4)
        mesh.add(mesh5)
        mesh.add(mesh6)
        mesh.add(mesh7)
        mesh.add(mesh8)
        mesh.add(mesh9)
        mesh.add(mesh10)
        mesh.add(mesh11)

        return mesh
