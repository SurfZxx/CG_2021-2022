import OpenGL.GL as GL


from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform

class Test(Base):
     """ Render shapes with vertex colors """
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

        # Set up vertex array object #
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        # Set up vertex attributes #
        position_data = [[-0.22, 0.24, 0.0], #E
                         [-0.29, 0.24, 0.0], #F
                         [-0.29, -0.28, 0.0], #O
                         [-0.22, -0.28, 0.0], #P
                         [-0.22, 0.24, 0.0], #E
                         [-0.22, -0.06, 0.0], #V
                         [-0.22, 0.02, 0.0], #U
                         [-0.29, 0.02, 0.0], #G
                         [-0.29, -0.06, 0.0], #N
                         [-0.52, 0.02, 0.0], #H
                         [-0.52, -0.06, 0.0], #M
                         [-0.29, -0.06, 0.0], #N
                         [-0.52, -0.06, 0.0], #M
                         [-0.52, 0.02, 0.0], #H
                         [-0.52, -0.28, 0.0], #L
                         [-0.59, -0.28, 0.0], #K
                         [-0.52, 0.24, 0.0], #I
                         [-0.59, 0.24, 0.0], #J
                         [-0.59, -0.28, 0.0]] #K
  
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')
        
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')

        self.base_color = Uniform('vec3', [0.0, 0.0, 1.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.dx = 0.01
        self.dy = 0.01
       
     def update(self):
        """debug printing"""

    

        if (self.input.isKeyPressed("up") > 0 and 0.755 > self.translation.data[1]):
            self.translation.data[1] += self.dy
        if (self.input.isKeyPressed("right") > 0 and 1.22 > self.translation.data[0]):
            self.translation.data[0] += self.dx
        if (self.input.isKeyPressed("down") > 0 and self.translation.data[1] > -0.72):
            self.translation.data[1] -= self.dy
        if (self.input.isKeyPressed("left") > 0 and self.translation.data[0] > -0.41):
            self.translation.data[0] -= self.dx

    
        GL.glClearColor(0, 0, 0, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, self.vertex_count)

# instantiate this class and run the program
Test().run()