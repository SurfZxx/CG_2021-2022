"""Passar dados entre shaders"""
import OpenGL.GL as GL


from core.base import Base
from core.utils import Utils
from core.attribute import Attribute


class Example(Base):
    """ Render shapes with vertex colors """
    def initialize(self):
        print("Initializing program...")

        # Initialize program #
        vs_code = """
            in vec3 position;
            in vec3 vertexColor;
            out vec3 color;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
                color = vertexColor;
            }
        """
        fs_code = """
            in vec3 color;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(color.r, color.g, color.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings (optional) #
        GL.glPointSize(10)
        GL.glLineWidth(4)
        
        # Set up vertex array object - letter_h #
        self.vao_letter_h = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_letter_h)
        position_data_letter_h = [[-0.22, 0.27, 0.0], #E
                         [-0.29, 0.27, 0.0], #F
                         [-0.29, -0.25, 0.0], #O
                         [-0.22, -0.25, 0.0], #P
                         [-0.22, 0.27, 0.0], #E
                         [-0.22, -0.03, 0.0], #V
                         [-0.22, 0.05, 0.0], #U
                         [-0.29, 0.05, 0.0], #G
                         [-0.29, -0.03, 0.0], #N
                         [-0.52, 0.05, 0.0], #H
                         [-0.52, -0.03, 0.0], #M
                         [-0.29, -0.03, 0.0], #N
                         [-0.52, -0.03, 0.0], #M
                         [-0.52, 0.05, 0.0], #H
                         [-0.52, -0.25, 0.0], #L
                         [-0.59, -0.25, 0.0], #K
                         [-0.52, 0.27, 0.0], #I
                         [-0.59, 0.27, 0.0], #J
                         [-0.59, -0.25, 0.0]] #K
        self.vertex_count_letter_h = len(position_data_letter_h)
        position_attribute_letter_h = Attribute('vec3', position_data_letter_h)
        position_attribute_letter_h.associate_variable(self.program_ref, 'position')
        
        # Set up vertex array object #
        self.vao_letter_s = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_letter_s)
        # Set up vertex attributes #
        position_data_letter_s = [[0.35, 0.07, 0.0], #C
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
        self.vertex_count_letter_s = len(position_data_letter_s)
        position_attribute_letter_s = Attribute("vec3", position_data_letter_s)
        position_attribute_letter_s.associate_variable(self.program_ref, 'position')
        color_data = [[0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0],
                        [0.0, 0.0, 1.0]]
        color_attribute = Attribute("vec3", color_data)
        color_attribute.associate_variable(self.program_ref, 'vertexColor')

    def update(self):
        GL.glUseProgram(self.program_ref)
                # Draw the letter_h
        GL.glBindVertexArray(self.vao_letter_h)
        # GL.glDrawArrays(GL.GL_POINTS, 0, self.vertex_count_letter_h)
        # GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count_letter_h)
        # GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_letter_h)
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count_letter_h)
        
        # Draw the letter_s
        GL.glBindVertexArray(self.vao_letter_s)
        # GL.glDrawArrays(GL.GL_POINTS, 0, self.vertex_count_letter_s)
        # GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_letter_s)
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count_letter_s)


# Instantiate this class and run the program
Example().run()
