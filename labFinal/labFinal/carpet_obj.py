from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial

class CarpetObject(Base):
    def initialize():
        carpet = RectangleGeometry(width=6, height=3)

        carpet_texture = Texture(file_name="images/carpet.jpg")
        carpet_material = TextureMaterial(texture=carpet_texture)

        mesh = Mesh(carpet, carpet_material)
        
    
        mesh.translate(0, 0, 0)
        
        return mesh