from turtle import position
from geometry.cylindrical import CylindricalGeometry


class PyramidGeometry(CylindricalGeometry):
    def __init__(self, radius=1, height=1, sides=4, height_segments=4, closed=True):
        super().__init__()#0, radius, height, sides, height_segments, False, #closed)
        # vertices
        p0 = [-height, -height, -height]
        p1 = [height, -height, -height]
        p2 = [-height, height, -height]
        p3 = [height, height, -height]
        p4 = [-height, -height, height]
        # colors for faces in order:
        c1, c2 = [1, 0.5, 0.5], [0.5, 0, 0]
        c3, c4 = [0.5, 1, 0.5], [0, 0.5, 0]
        c5 = [0.5, 0.5, 1]
        
        # texture coordinates
        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]
        
        position_data = [p0,p1,p2,
                         p2,p1,p3,
                         p3,p4,p1,
                         p4,p1,p0]
        color_data = [c1] * 5 + [c2] * 5 + [c3] * 5 \
                   + [c4] * 5 + [c5] * 5
        uv_data = [t0, t1, t3, t0, t3, t2] * 5
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()