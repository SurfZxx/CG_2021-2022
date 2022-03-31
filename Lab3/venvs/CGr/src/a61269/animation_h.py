"""Letter moves along a circular path"""
import math
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate letter moving in a circular path around the origin """
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # Render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 1.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        # new_x = x + 0.42
        position_data = [[0.2, 0.24, 0.0], #E
                         [0.13, 0.24, 0.0], #F
                         [0.13, -0.28, 0.0], #O
                         [0.2, -0.28, 0.0], #P
                         [0.2, 0.24, 0.0], #E
                         [0.2, -0.06, 0.0], #V
                         [0.2, 0.02, 0.0], #U
                         [0.13, 0.02, 0.0], #G
                         [0.13, -0.06, 0.0], #N
                         [-0.1, 0.02, 0.0], #H
                         [-0.1, -0.06, 0.0], #M
                         [0.13, -0.06, 0.0], #N
                         [-0.1, -0.06, 0.0], #M
                         [-0.1, 0.02, 0.0], #H
                         [-0.1, -0.28, 0.0], #L
                         [-0.17, -0.28, 0.0], #K
                         [-0.1, 0.24, 0.0], #I
                         [-0.17, 0.24, 0.0], #J
                         [-0.17, -0.28, 0.0]] #K
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [-0.5, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.0, 0.0, 1.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        """ Update data """
        self.translation.data[0] = 0.7 * math.sin(self.time)
        self.translation.data[1] = 0.7 * math.cos(self.time)
        
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        # GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()