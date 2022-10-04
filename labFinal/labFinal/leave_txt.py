from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial
from extras.text_texture import TextTexture

class leaveObject(Base):
    def initialize():
        leave_text_box = RectangleGeometry(width=1.5, height=0.3)

        leave_texttexture = TextTexture(text=" To Leave press 'm' ",
                 system_font_name="Arial", font_file_name=None,
                 font_size=24, font_color=[0,0,0],
                 background_color=[255,255,255], transparent=False,
                 image_width=None, image_height=None,
                 align_horizontal=0.0, align_vertical=0.0,
                 image_border_width=0, image_border_color=[0,0,0])
        leave_textmaterial = TextureMaterial(texture=leave_texttexture)

        mesh = Mesh(leave_text_box, leave_textmaterial)
        
        mesh.translate(0, 0, 0)
        
        return mesh