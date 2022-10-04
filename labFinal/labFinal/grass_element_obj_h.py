from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial

class grassObject_h(Base):
    def initialize():
        grass_element = RectangleGeometry(width=1, height=1)

        grass_texture = Texture(file_name="images/grass_symbol.jpg")
        grass_material = TextureMaterial(texture=grass_texture)

        mesh = Mesh(grass_element, grass_material)
        
        mesh.translate(0, 0, 0)
        
        return mesh