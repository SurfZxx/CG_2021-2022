"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from geometry.rectangle import RectangleGeometry
from material.surface import SurfaceMaterial
from material.point import PointMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class CarpetObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def getObj():
        carpet = RectangleGeometry(width=6, height=3)

        #material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})
        material = SurfaceMaterial(property_dict={"useVertexColors": True})
        #material = SurfaceMaterial(
        #    property_dict= {
        #        "useVertexColors": True,
        #        "wireframe": True,
        #        "lineWidth": 8
        #    }
        #)

        carpet_texture = Texture(file_name="images/carpet.jpg")
        carpet_material = TextureMaterial(texture=carpet_texture)

        mesh = Mesh(carpet, carpet_material)
        
    
        mesh.translate(0, 0, 0)
        

        return mesh


# Instantiate this class and run the program
CarpetObject(screen_size=[1000, 800]).run()