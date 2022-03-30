"""Changing color with time"""
import math
import OpenGL.GL as GL


from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform


class Example(Base):
    """ Animate triangle changing its color """
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
        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attribute #
        position_data = [[0.35, 0.07, 0.0], #C
                                [0.43, 0.07, 0.0], #D
                                [0.35, 0.09, 0.0], #E
                                [0.42, 0.13, 0.0], #F
                                [0.34, 0.11, 0.0], #G
                                [0.39, 0.17, 0.0], #H
                                [0.32, 0.12, 0.0], #I
                                [0.34, 0.19, 0.0], #J
                                [0.31, 0.12, 0.0], #K
                                [0.29, 0.19, 0.0], #L
                                [0.29, 0.12, 0.0], #M
                                [0.25, 0.19, 0.0], #N
                                [0.27, 0.12, 0.0], #O
                                [0.21, 0.17, 0.0], #P
                                [0.25, 0.11, 0.0], #Q
                                [0.18, 0.12, 0.0], #R
                                [0.24, 0.09, 0.0], #S
                                [0.17, 0.08, 0.0], #T
                                [0.24, 0.07, 0.0], #U
                                [0.17, 0.05, 0.0], #V
                                [0.25, 0.05, 0.0], #W
                                [0.17, 0.01, 0.0], #Z
                                [0.26, 0.03, 0.0], #A1
                                [0.19, -0.03, 0.0], #B1
                                [0.29, 0.01, 0.0], #C1
                                [0.24, -0.07, 0.0], #D1
                                [0.36, -0.03, 0.0], #E1
                                [0.33, -0.12, 0.0], #F1
                                [0.4, -0.05, 0.0], #G1
                                [0.35, -0.14, 0.0], #H1
                                [0.43, -0.09, 0.0], #I1
                                [0.36, -0.16, 0.0], #J1
                                [0.44, -0.16, 0.0], #K1
                                [0.36, -0.18, 0.0], #L1
                                [0.43, -0.21, 0.0], #M1
                                [0.35, -0.2, 0.0], #N1
                                [0.4, -0.26, 0.0], #O1
                                [0.33, -0.21, 0.0], #P1
                                [0.37, -0.29, 0.0], #Q1
                                [0.3, -0.22, 0.0], #R1
                                [0.32, -0.3, 0.0], #S1
                                [0.28, -0.22, 0.0], #T1
                                [0.26, -0.3, 0.0], #U1
                                [0.26, -0.21, 0.0], #V1
                                [0.2, -0.27, 0.0], #W1
                                [0.25, -0.19, 0.0], #Z1
                                [0.17, -0.22, 0.0], #A2
                                [0.16, -0.17, 0.0], #B2
                                [0.24, -0.17, 0.0], #C2
                                [0.25, -0.19, 0.0]] #Z1
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.0, 0.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

    def update(self):
        """ Update data """
        # Fast change, note 3 * self.time
        # self.base_color.data[0] = (math.sin(3 * self.time) + 1) / 2
        # self.base_color.data[0] = (math.sin(self.time) + 1) / 2
        # self.base_color.data[1] = (math.sin(self.time + 2.1) + 1) / 2
        self.base_color.data[2] = (math.sin(self.time + 4.2) + 1) / 2
        ## Render scene
        # Reset color buffer with specified color
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count)


# Instantiate this class and run the program
Example().run()