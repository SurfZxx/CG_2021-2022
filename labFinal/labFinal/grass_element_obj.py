from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class grassObject(Base):
    def initialize():
        grass_element = RectangleGeometry(width=1, height=1)
        grass_text_box = RectangleGeometry(width=1, height=0.25)

        grass_texture = Texture(file_name="images/grass_symbol.jpg")
        grass_material = TextureMaterial(texture=grass_texture)

        grass_texttexture = TextTexture(text="Grass (Press L)",
                 system_font_name="Arial", font_file_name=None,
                 font_size=24, font_color=[0,0,0],
                 background_color=[255,255,255], transparent=False,
                 image_width=None, image_height=None,
                 align_horizontal=0.0, align_vertical=0.0,
                 image_border_width=0, image_border_color=[0,0,0])
        grass_textmaterial = TextureMaterial(texture=grass_texttexture)

        mesh = Mesh(grass_element, grass_material)
        mesh1 = Mesh(grass_text_box, grass_textmaterial)
        
    
        mesh.translate(0, 0, 0)
        mesh1.translate(0, -0.625, 0)

        mesh.add(mesh1)
        
        return mesh