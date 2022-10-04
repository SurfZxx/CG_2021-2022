from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class winObject(Base):
    def initialize():
        win_text_box = RectangleGeometry(width=3, height=1)

        win_texttexture = TextTexture(text=" You Win ",
                 system_font_name="Arial", font_file_name=None,
                 font_size=32, font_color=[0,0,0],
                 background_color=[255,255,255], transparent=False,
                 image_width=None, image_height=None,
                 align_horizontal=0.0, align_vertical=0.0,
                 image_border_width=0, image_border_color=[0,0,0])
        win_textmaterial = TextureMaterial(texture=win_texttexture)

        mesh = Mesh(win_text_box, win_textmaterial)
        
        mesh.translate(0, 0, 0)
        
        return mesh