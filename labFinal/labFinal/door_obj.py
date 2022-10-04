from core.base import Base
from core_ext.mesh import Mesh
from geometry.bedbox import BoxGeometry
from geometry.black_box import BlackBox
from geometry.sphere import SphereGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

class doorObject(Base):
    def initialize():
        door = BoxGeometry(width=0.1, height=2.9, depth=1.7)
        door_knob = SphereGeometry(radius=0.05, radius_segments=32, height_segments=16)
        
        door_texture = Texture(file_name="images/door-texture.jpg")
        door_material = TextureMaterial(texture=door_texture)
        
        metal_texture = Texture(file_name="images/metal.jpg")
        metal_material = TextureMaterial(texture=metal_texture)
        
        mesh = Mesh(door, door_material)
        mesh1 = Mesh(door_knob, metal_material)
        
        mesh1.translate(-0.08, -0.15, 0.75)
        
        mesh.add(mesh1)
        
        return mesh