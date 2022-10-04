from core.base import Base
from core_ext.mesh import Mesh
from geometry.bedbox import BoxGeometry
from geometry.black_box import BlackBox
from geometry.sphere import SphereGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

class posterObject(Base):
    def initialize():
        plate = BoxGeometry(width=0.1, height=0.7, depth=0.7)
        border = BlackBox(width=0.1, height=0.8, depth=0.8)
        
        poster_texture = Texture(file_name="images/pepe_hand.jpg")
        poster_material = TextureMaterial(texture=poster_texture)
        
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        
        mesh = Mesh(plate, poster_material)
        mesh1 = Mesh(border, material)
        
        mesh1.translate(-0.01,0,0)
        
        mesh.add(mesh1)
        
        return mesh