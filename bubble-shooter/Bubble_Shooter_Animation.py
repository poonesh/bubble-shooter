 

from Bubble_Tkinter import TKPICTURE
from Bubble_Line_Shooter import LineShooter 
from Bubble import Bubble



tk_canvas = TKPICTURE(600, 600)
line_shoot = LineShooter(tk_canvas)
next_bubble = Bubble(tk_canvas)
last_bubble = None
stuck_balls = set([])
list_of_grids = next_bubble.make_grid()



# event_handler function
def update_line_vel_right_press(event): 
	line_shoot.update_vel_right_press(line_shoot.firing_angle_vel_inc)



# event handler function 
def update_line_vel_left_press(event):
	line_shoot.update_vel_left_press(line_shoot.firing_angle_vel_inc)



# event_handler function
def update_line_vel_right_release(event): 
	line_shoot.update_vel_right_release(line_shoot.firing_angle_vel_inc)



# event handler function 
def update_line_vel_left_release(event):
	line_shoot.update_vel_left_release(line_shoot.firing_angle_vel_inc)



def update_line():
	line_shoot.update_line_angle_add(line_shoot.firing_angle_vel)




def shoot_Bubble(event):
	global last_bubble, next_bubble
	next_bubble.fire_Bubble(10, line_shoot.firing_angle)
	last_bubble = next_bubble
 	next_bubble = None
 	



def last_bubble_stuck(): 
	global last_bubble
	if last_bubble is not None:
		# print len(stuck_balls) 
		if last_bubble.is_stuck(stuck_balls, list_of_grids):
			last_bubble.build_adj_dict(stuck_balls)
			return True
		
	return False




def load_Bubble():
	global next_bubble, last_bubble
	if last_bubble_stuck() and next_bubble == None:
		next_bubble = Bubble(tk_canvas)



# def build_adjacent_dict(): # why load bubble did not work if I put build dict in the line before next_bubble = 0.
# 	global next_bubble, last_bubble
# 		last_bubble.build_adj_dict(stuck_balls)
		
	


tk_canvas.canvas.focus_set()
tk_canvas.up_arrow(shoot_Bubble)
tk_canvas.right_arrow_press(update_line_vel_right_press)
tk_canvas.left_arrow_press(update_line_vel_left_press)
tk_canvas.right_arrow_release(update_line_vel_right_release)
tk_canvas.left_arrow_release(update_line_vel_left_release)
tk_canvas.render_loop(last_bubble_stuck, update_line, load_Bubble) 






