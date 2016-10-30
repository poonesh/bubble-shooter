

import math
from Tkinter import *



# this function provides angle to a vector
def ang_to_vec(ang):
    return[math.cos(ang), math.sin(ang)] 



class LineShooter(object):

    def __init__(self, TK_pic):
        self.tk_pic = TK_pic
        self.firing_angle = - math.pi/2
        self.firing_angle_add = 0.05
        self.firing_angle_vel = 0
        self.line_length = 100
        self.firing_angle_vel_inc = 0.03

        
        vec = ang_to_vec(self.firing_angle)


        self.x0 = self.tk_pic.width/2
        self.y0 = self.tk_pic.height
        self.x1 = self.x0 + self.line_length * vec[0] 
        self.y1 = self.y0 + self.line_length * vec[1]


        self.line_index = self.tk_pic.create_line(self.x0, self.y0, self.x1, self.y1, width=4.0, fill= "white")
        self.tk_pic.shapesLine[self.line_index] = self



    def update_line_angle_add(self, firing_angle_vel):
        # updating the line and constraining it to Tkinter Canvas

        if self.firing_angle + firing_angle_vel < 0 and self.firing_angle + firing_angle_vel > -math.pi:
            self.firing_angle += firing_angle_vel
           
        
        vec = ang_to_vec(self.firing_angle)

        self.x1 = self.x0 + self.line_length * vec[0]
        self.y1 = self.y0 + self.line_length * vec[1]

        self.tk_pic.coords(self.line_index, self.x0, self.y0, self.x1, self.y1)




    def update_vel_left_press(self, vel_inc):
        self.firing_angle_vel -= vel_inc



    def update_vel_left_release(self, vel_inc):
        self.firing_angle_vel += vel_inc



    def update_vel_right_press(self, vel_inc):
        self.firing_angle_vel += vel_inc



    def update_vel_right_release(self, vel_inc):
        self.firing_angle_vel -= vel_inc                                                     


















        




