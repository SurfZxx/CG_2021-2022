from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class loseObject(Base):
    def initialize():
        lose_text_box = RectangleGeometry(width=3, height=1)

        lose_texttexture = TextTexture(text=" You Lose ",
                 system_font_name="Arial", font_file_name=None,
                 font_size=32, font_color=[0,0,0],
                 background_color=[255,255,255], transparent=False,
                 image_width=None, image_height=None,
                 align_horizontal=0.0, align_vertical=0.0,
                 image_border_width=0, image_border_color=[0,0,0])
        lose_textmaterial = TextureMaterial(texture=lose_texttexture)

        mesh = Mesh(lose_text_box, lose_textmaterial)
        
        mesh.translate(0, 0, 0)
        
        return mesh