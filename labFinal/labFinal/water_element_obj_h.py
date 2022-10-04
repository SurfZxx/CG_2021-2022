from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial

class waterObject_h(Base):
    def initialize():
        water_element = RectangleGeometry(width=1, height=1)

        water_texture = Texture(file_name="images/water_symbol.jpg")
        water_material = TextureMaterial(texture=water_texture)

        mesh = Mesh(water_element, water_material)
        
        mesh.translate(0, 0, 0)
        
        return mesh