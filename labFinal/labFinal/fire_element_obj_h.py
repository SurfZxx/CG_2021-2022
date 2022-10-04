from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial

class fireObject_h(Base):
    def initialize():
        fire_element = RectangleGeometry(width=1, height=1)

        fire_texture = Texture(file_name="images/fire_symbol.jpg")
        fire_material = TextureMaterial(texture=fire_texture)

        mesh = Mesh(fire_element, fire_material)
        
        mesh.translate(0, 0, 0)
        
        return mesh