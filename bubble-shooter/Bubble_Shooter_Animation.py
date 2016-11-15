 

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
		if last_bubble.is_stuck(stuck_balls, list_of_grids):
			return True	
	return False



def make_adj_dict():
	if last_bubble_stuck():
		last_bubble.adj_dict = last_bubble.build_adj_dict(stuck_balls)



def make_bubble_chain():
	same_color_chain_list = []
	chain_list = last_bubble.get_bubble_chain(same_color_chain_list)
	print chain_list
	print len(chain_list)
	if len(chain_list) >= 3:
		for bubble in chain_list:
			tk_canvas.delete_widget(bubble.Bubble_index)
			stuck_balls.remove(bubble)
		last_bubble.bubble_chain_delete(same_color_chain_list)



def renderHandler():
	if last_bubble_stuck():
		make_adj_dict()
		make_bubble_chain()
		load_Bubble()


	
def load_Bubble():
	global next_bubble, last_bubble
	if next_bubble == None:
		last_bubble = None
		next_bubble = Bubble(tk_canvas)



tk_canvas.canvas.focus_set()
tk_canvas.up_arrow(shoot_Bubble)
tk_canvas.right_arrow_press(update_line_vel_right_press)
tk_canvas.left_arrow_press(update_line_vel_left_press)
tk_canvas.right_arrow_release(update_line_vel_right_release)
tk_canvas.left_arrow_release(update_line_vel_left_release)
tk_canvas.render_loop(renderHandler, update_line) 



