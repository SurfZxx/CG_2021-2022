from core.base import Base
from core_ext.mesh import Mesh
from geometry.bedbox import BoxGeometry
from geometry.sphere import SphereGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class bedObject(Base):
    
    def initialize():
        
        
        bottom = BoxGeometry(width=2.8, height=0.6, depth=1.6)
        cushion = BoxGeometry(width=2.7, height=0.2, depth=1.5)
        plate = BoxGeometry(width=0.3, height=1, depth=1.6)
        darkwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkwood_material = TextureMaterial(texture=darkwood_texture)
        
        
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        mesh = Mesh(bottom, darkwood_material)
        mesh1 = Mesh(cushion, material)
        mesh2 = Mesh(plate, darkwood_material)
        
        mesh1.translate(0,0.3,0)
        mesh2.translate(-1.5,0.2,0)
        mesh.add(mesh1)
        mesh.add(mesh2)
        
        
        # meshMaster = Mesh(geometry1, material)
        
        return mesh
        