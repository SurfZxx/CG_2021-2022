import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute

class Example(Base):
    
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            void main()
            {
                gl_Position = vec4(position.x, position.y, position.z, 1.0);
            }
        """
        fs_code = """
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(1.0, 0.5, 0.0, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)
        # render settings #
        GL.glLineWidth(4)
        
        # Set up vertex array object - pentagon #
        self.vao_pentagon = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_pentagon)
        position_data_pentagon = [[0.64, 0.19, 0.0],
                                [0.0, 0.66, 0.0],
                                [-0.64, 0.19, 0.0],
                                [-0.4, -0.56, 0.0],
                                [0.4, -0.56, 0.0]]
        self.vertex_count_pentagon = len(position_data_pentagon)
        position_attribute_pentagon = Attribute('vec3', position_data_pentagon)
        position_attribute_pentagon.associate_variable(self.program_ref, 'position')

    def update(self):
        # Using same program to render the pentagon
        GL.glUseProgram(self.program_ref)
        
        # Draw the pentagon
        GL.glBindVertexArray(self.vao_pentagon)
        # GL.glDrawArrays(GL.GL_POINTS, 0, self.vertex_count_pentagon)
        # GL.glDrawArrays(GL.GL_LINE_LOOP, 0, self.vertex_count_pentagon)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN, 0, self.vertex_count_pentagon)

# Instantiate this class and run the program
Example().run()