"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial

from geometry.box import BoxGeometry
from geometry.sphere import SphereGeometry

class tvObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():

        geo_screen = BoxGeometry(width=0.01, height=1.5, depth=2.9)
        geo_backScreen  = BoxGeometry(width=0.05, height=1.5, depth=2.9)
        geo_screenBase  = BoxGeometry(width=0.05, height=0.05, depth=0.25)
        geo_topBorder   = BoxGeometry(width=0.10, height=0.05, depth=3)
        geo_sideBorder  = BoxGeometry(width=0.10, height=1.5, depth=0.065)
        # geo_topBorder = SphereGeometry(radius=0.05, radius_segments=0.10, height_segments=3.2)

        material = SurfaceMaterial(property_dict={"useVertexColors": True})

        tv_texture = Texture(file_name="images/tv_background.jpg")
        tv_material = TextureMaterial(texture=tv_texture)

        tv_borderTexture = Texture(file_name="images/black.jpg")
        tv_borderMaterial = TextureMaterial(texture=tv_borderTexture)

        meshMaster = Mesh(geo_screen, tv_material)       # Front Screen 
        mesh1 = Mesh(geo_backScreen, tv_borderMaterial) # Back Screen
        mesh2 = Mesh(geo_screenBase, tv_borderMaterial) # Left base of the screen
        mesh3 = Mesh(geo_screenBase, tv_borderMaterial) # Right base of the screen
        mesh4 = Mesh(geo_topBorder,  tv_borderMaterial)  # Top border of the screen
        mesh5 = Mesh(geo_topBorder,  tv_borderMaterial)  # Top bottom of the screen
        mesh6 = Mesh(geo_sideBorder, tv_borderMaterial)  # Left border of the screen
        mesh7 = Mesh(geo_sideBorder, tv_borderMaterial)  # Right border of the screen
        
        meshMaster.rotate_y(1.57079632679)

        mesh1.translate(0.02,0,0)

        mesh2.translate(0,-0.80,-1.4)
        mesh2.rotate_y(-1.57079632679)

        mesh3.translate(0,-0.80,1.4)
        mesh3.rotate_y(-1.57079632679)

        mesh4.translate(0,0.75,0)

        mesh5.translate(0,-0.75,0)

        mesh6.translate(0,0,-1.467)

        mesh7.translate(0,0,1.467)
        
        meshMaster.add(mesh1)
        meshMaster.add(mesh2) 
        meshMaster.add(mesh3)
        meshMaster.add(mesh4)
        meshMaster.add(mesh5)
        meshMaster.add(mesh6)
        meshMaster.add(mesh7)

        return(meshMaster)