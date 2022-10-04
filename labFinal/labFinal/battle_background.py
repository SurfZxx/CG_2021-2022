from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from geometry.sphere import SphereGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial

class battleBackground(Base):
    def initialize():
        battlecamp = RectangleGeometry(width=10, height=5)

        battle_texture = Texture(file_name="images/floor_texture.jpg")
        battle_material = TextureMaterial(texture=battle_texture)

        mesh = Mesh(battlecamp, battle_material)
        
    
        mesh.translate(0, 0, 0)
        
        return mesh