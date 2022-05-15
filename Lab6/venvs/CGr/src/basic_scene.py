"""An example of a basic scene: spinning cube"""

from core.base import Base
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial

from geometry.object1 import BoxGeometry1
from geometry.object2 import BoxGeometry2
from geometry.object3 import SphereGeometry

class closetObject(Base):
    """ Render a basic scene that consists of a spinning cube """
    def closet():

        geometry1 = BoxGeometry1()
        geometry2 = SphereGeometry()
        geometry3 = BoxGeometry2()

        # material = PointMaterial(property_dict={"baseColor": [1, 1, 0], "pointSize": 5})

        material = SurfaceMaterial(property_dict={"useVertexColors": True})

        # material = SurfaceMaterial(
        #     property_dict= {
        #         "useVertexColors": True,
        #         "wireframe": True,
        #         "lineWidth": 8
        #     }
        # )

        meshMaster = Mesh(geometry1, material)

        mesh1 = Mesh(geometry1, material)
        mesh2 = Mesh(geometry1, material)
        mesh3 = Mesh(geometry3, material)
        mesh4 = Mesh(geometry2, material)
        mesh5 = Mesh(geometry2, material)

        mesh1.translate(-0.5,0,0)
        mesh2.translate(0.0,0,0)
        mesh3.translate(-0.25,1,0)
        mesh4.translate(0,0,+0.525)
        mesh5.translate(-0.5,0,+0.525)
        
        meshMaster.add(mesh1)
        meshMaster.add(mesh2)
        meshMaster.add(mesh3)
        meshMaster.add(mesh4)
        meshMaster.add(mesh5)

        meshMaster.translate(+0.25,0,0)

        return(meshMaster)