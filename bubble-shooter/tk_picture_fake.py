

from Tkinter import *

class FAKE_TKPICTURE(object):

	def __init__(self, width, height):
		self.master = Tk()
		self.width = width
		self.height = height
		self.canvas = Canvas(self.master, bg="black", width= self.width, height= self.height)
		self.canvas.pack()

		self.shapesLine = {} 
		self.shapesBubble = {} 

		
	def update(self):
		pass 

	
	# updating every frame
	def render_loop(self, func2call_1, func2call_2, func2call_3):
		pass


	# to update moving widget on canvas, we need to use coords or move (like canvas.coords(index_of_the_widget, x0, y0, x1, y1))
	def coords(self, index, x0, y0, x1, y1):
		pass 
		


	def create_oval(self, x0, y0, x1, y1, outline = "grey", fill = "red", width = 1):
		pass
		


	def create_line(self, x0, y0, x1, y1, width=4.0, fill= "white"):
		pass
		

	# binding Right_arrow
	def right_arrow_press(self, update_line_vel_right_press):
		pass
		

	def right_arrow_release(self, update_line_vel_right_release):
		pass
		
	
	# binding Left_arrow 
	def left_arrow_press(self, update_line_vel_left_press):
		pass
		

	def left_arrow_release(self, update_line_vel_left_release):
		pass
		

	# binding Up_arrow
	def up_arrow(self, shoot_Bubble):
		pass
		





