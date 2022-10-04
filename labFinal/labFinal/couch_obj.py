"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from geometry.box import BoxGeometry
from material.surface import SurfaceMaterial
from core_ext.texture import Texture
from material.texture import TextureMaterial


class CouchObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize():
        couchbase = BoxGeometry(width=2, height=0.6, depth=1.5)
        couch_side = BoxGeometry(width=0.3, height=1.3, depth=1.5)
        couchbase_pillow = BoxGeometry(width=1.75, height=0.2, depth=1.6)
        couchback_pillow = BoxGeometry(width=2.155, height=1, depth=0.2)
        couch_back = BoxGeometry(width=2.15, height=1.8, depth=0.25)

        darkbrownwood_texture = Texture(file_name="images/dark-brown-wood.jpg")
        darkbrownwood_material = TextureMaterial(texture=darkbrownwood_texture)

        sofa_texture = Texture(file_name="images/sofa_texture.jpg")
        sofa_material = TextureMaterial(texture=sofa_texture)



        mesh = Mesh(couchbase, darkbrownwood_material)
        mesh1 = Mesh(couch_side, darkbrownwood_material)
        mesh2 = Mesh(couch_side, darkbrownwood_material)
        mesh3 = Mesh(couchbase_pillow, sofa_material)
        mesh4 = Mesh(couch_back, darkbrownwood_material)
        mesh5 = Mesh(couchback_pillow, sofa_material)
    
        mesh.translate(0, -0.5, 0)
        mesh1.translate(1, 0.1, 0)
        mesh2.translate(-1, 0.1, 0)
        mesh3.translate(0, 0.25, 0)
        mesh4.translate(0, 0.4, -0.7)
        mesh5.translate(0, 0.75, -0.65)

        mesh.add(mesh1)
        mesh.add(mesh2)
        mesh.add(mesh3)
        mesh.add(mesh4)
        mesh.add(mesh5)


        return mesh
