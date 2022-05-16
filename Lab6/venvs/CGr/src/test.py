from random import uniform
import numpy as np
import math
import pathlib
import sys
import OpenGL.GL as GL
from OpenGL.GL import *
import pygame

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.movement_rig import MovementRig
from material.surface import SurfaceMaterial
from core.obj_reader import my_obj_reader
from core.utils import Utils
from core.uniform import Uniform
from core.attribute import Attribute
from core.matrix import Matrix
from math import *

class Test(Base):
    
    def load_texture(path, texture):
        GL.glBindTexture(GL.GL_TEXTURE_2D, texture)
        # Set the texture wrapping parameters
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        # Set texture filtering parameters
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        # load image
        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA, image.width, image.height, 0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img_data)
        return 


    def initialize(self):
        """Setup the object and shaders"""
        print('Initializing program...')
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        ### Initialize program ###
        vs_code = """
            in vec3 position;
            uniform mat4 projectionMatrix;
            uniform mat4 modelMatrix;
            void main()
            {
                gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
            }
        """
        fs_code = """
            in vec3 color;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(1.0,1.0,1.0, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)

        ### Render settings ###
        GL.glClearColor(0.0, 1.0, 0.0, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        self.textures = GL.glGenTextures(1)
        self.load_texture("core/wood_solid.jpg", self.textures[1])
        
        ### Set up vertex array object ###
        vao_ref = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vao_ref)
        ### Set up vertex attribute: three points of triangle ###
        # position_data = [[0.0,   0.2,  0.0], [0.1,  -0.2,  0.0], [-0.1, -0.2,  0.0]]
        ### Set up vertex attribute: reading the blender model

        position_data = my_obj_reader('core/bedroom.obj')
        self.vertex_count = len(position_data)
        position_attribute = Attribute('vec3', position_data)
        position_attribute.associate_variable(self.program_ref, 'position')

        ### Set up uniforms ###
        m_matrix = Matrix.make_translation(0, 0, -1)
        self.model_matrix = Uniform('mat4', m_matrix)
        self.model_matrix.locate_variable(self.program_ref, 'modelMatrix')
        p_matrix = Matrix.make_perspective()
        self.projection_matrix = Uniform('mat4', p_matrix)
        self.projection_matrix.locate_variable(self.program_ref, 'projectionMatrix')
        
        # movement speed, units per second
        self.move_speed = 2
        # rotation speed, radians per second
        self.turn_speed = 90 * (pi / 180)
        

    def update(self):
        """ Update data """
        
        move_amount = self.move_speed * self.delta_time
        turn_amount = self.turn_speed * self.delta_time
        
        if self.input.is_key_pressed('w'):
            m = Matrix.make_translation(0, 0, move_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('s'):            
            m = Matrix.make_translation(0, 0, -move_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('a'):
            m = Matrix.make_translation(move_amount, 0, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('d'):
            m = Matrix.make_translation(-move_amount, 0, 0)            
            self.model_matrix.data = m @ self.model_matrix.data
        
        
        if self.input.is_key_pressed('q'):
            m = Matrix.make_rotation_y(-turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('e'):
            m = Matrix.make_rotation_y(turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('r'):
            m = Matrix.make_translation(0, -move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('f'):
            m = Matrix.make_translation(0, move_amount, 0)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('t'):
            m = Matrix.make_rotation_x(-turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        if self.input.is_key_pressed('g'):
            m = Matrix.make_rotation_x(turn_amount)
            self.model_matrix.data = m @ self.model_matrix.data
        
        ### Render scene ###
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)
        
        # GL.glDrawArrays(GL.GL_POINTS, 0, self.vertex_count)

        self.renderer.render(self.scene, self.camera)
        self.projection_matrix.upload_data()
        self.model_matrix.upload_data()
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.textures[1])
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, self.vertex_count)
        # GL.glDrawArrays(GL.GL_LINES, 0, self.vertex_count)
                
Test(screen_size=[800, 600]).run()