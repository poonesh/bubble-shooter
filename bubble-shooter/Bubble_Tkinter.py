
from Tkinter import *


"""
This class creates a customized (instance) of Canvas Tkinter, with width and height arguments.
"""

class TKPICTURE(object):

	def __init__(self, width, height):
		self.master = Tk()
		self.width = width
		self.height = height
		self.canvas = Canvas(self.master, bg="black", width= self.width, height= self.height)
		self.canvas.pack()

		self.shapesLine = {} 
		self.shapesBubble = {}    # shapeBubble dictionary to keep track of the instances of the Bubble class
		 

	def update(self):
		self.master.update()

	
	# updating every frame
	def render_loop(self, func2call_1, func2call_2):
		
		while True:

			for item in self.shapesBubble:
				shape = self.shapesBubble[item]
				shape.update_Bubble()
				shape.check_boundary()
				func2call_1()
			func2call_2()
					
			self.master.update()


	# to update moving widget on canvas, we need to use coords or move (like canvas.coords(index_of_the_widget, x0, y0, x1, y1))
	def coords(self, index, x0, y0, x1, y1): 
		self.canvas.coords(index, x0, y0, x1, y1)


	def create_oval(self, x0, y0, x1, y1, outline = "grey", fill = "red", width = 1):
		index_of_widget = self.canvas.create_oval(x0, y0, x1 , y1, outline = outline, fill = fill, width = width)
		return index_of_widget


	def create_line(self, x0, y0, x1, y1, width=4.0, fill= "white"):
		index_of_widget = self.canvas.create_line(x0, y0, x1, y1, width = width, fill = fill)
		return index_of_widget


	# binding Right_arrow
	def right_arrow_press(self, update_line_vel_right_press):
		return self.canvas.bind("<KeyPress-Right>", update_line_vel_right_press)


	def right_arrow_release(self, update_line_vel_right_release):
		return self.canvas.bind("<KeyRelease-Right>", update_line_vel_right_release)

	
	# binding Left_arrow 
	def left_arrow_press(self, update_line_vel_left_press):
		return self.canvas.bind("<KeyPress-Left>", update_line_vel_left_press)


	def left_arrow_release(self, update_line_vel_left_release):
		return self.canvas.bind("<KeyRelease-Left>", update_line_vel_left_release)

	
	# binding Up_arrow
	def up_arrow(self, shoot_Bubble):
		return self.canvas.bind("<Up>", shoot_Bubble)

	
	# binding space
	def space_button(self, load_Bubble):
		return self.canvas.bind("<space>", load_Bubble)







