
import random 
import math


# this functon provides distance between two points
def dist(p,q):
    return(math.sqrt((q[1]-p[1])**2+(q[0]-p[0])**2))


def ang_to_vec(ang):
    return[math.cos(ang), math.sin(ang)] 


class Bubble(object):
	
	def __init__(self, TK_pic, color=None):
		self.tk_pic = TK_pic
		self.Bubble_radius = 30
		self.Bubble_vel = [0, 0]
		self.Bubble_initial_pos = list([self.tk_pic.width/2, self.tk_pic.height])
		self.Bubble_last_pos = [0, 0]
		self.canv_width = 600
		self.canv_height = 600
		self.grid_width = 2*self.Bubble_radius
		self.grid_height = 2*self.Bubble_radius
		self.adj_dict = {}


		self.x0 = self.Bubble_initial_pos[0] - self.Bubble_radius
		self.y0 = self.Bubble_initial_pos[1] - self.Bubble_radius
		self.x1 = self.Bubble_initial_pos[0] + self.Bubble_radius
		self.y1 = self.Bubble_initial_pos[1] + self.Bubble_radius 

		
		if color is None:
			color_list = ["#6b8e23", "#ffd700", "#ff4500", "#f0fff0", "#0000cd"] 
			self.color = random.choice(color_list)
		else:
			self.color = color
		

		# create_oval takes two pairs of coordinates, top_left and bottom_right
		self.Bubble_index = self.tk_pic.create_oval(self.x0, self.y0, self.x1 , self.y1, outline = "grey", fill = self.color, width = 2)                                        
		# every Bubble has a unique index in the instance of the TKpic object. this index is stored in a dictionary
		# defined in the TKPICTURE class
		self.tk_pic.shapesBubble[self.Bubble_index] = self


	
	
	def fire_Bubble(self, vel, firing_angle):
		"""
		calculating velocity in the updated direction based on the firing line angle is passed
		"""

		vec = ang_to_vec(firing_angle)
		self.Bubble_vel = [vel*vec[0], vel*vec[1]]

	
	
	
	def update_Bubble(self):
		"""
		This function is called every frame in order to move the bubble by adding velocity to the current position.
		"""
		
		self.Bubble_initial_pos[0] += self.Bubble_vel[0]
		self.Bubble_initial_pos[1] += self.Bubble_vel[1]

		self.x0 = self.Bubble_initial_pos[0] - self.Bubble_radius
		self.y0 = self.Bubble_initial_pos[1] - self.Bubble_radius
		self.x1 = self.Bubble_initial_pos[0] + self.Bubble_radius
		self.y1 = self.Bubble_initial_pos[1] + self.Bubble_radius 

		self.tk_pic.coords(self.Bubble_index, self.x0, self.y0, self.x1, self.y1)




	def check_boundary(self):
		"""
		calculate the distance between the center of the bubble to the vertical boundaries
		so if a bubble hits a boundary the velocity will be reversed and the bubble will bounced back
		"""

		if self.Bubble_initial_pos[0] <= self.Bubble_radius or self.Bubble_initial_pos[0] >= self.tk_pic.width - self.Bubble_radius:
			self.Bubble_vel[0] = -self.Bubble_vel[0]

	

	def is_stuck(self, Set, list_of_grids):
		"""
		checking if the bubble hits the top boundary or checking against other bubbles in a set
		"""
	
		if self.Bubble_initial_pos[1] <= self.Bubble_radius:
			self.min_dist_grid(list_of_grids, self.Bubble_initial_pos)
			self.Bubble_vel = [0, 0]
			Set.add(self)
			return True

		for ball in set(Set):
			if dist(self.Bubble_initial_pos, ball.Bubble_initial_pos) <= (2.0*self.Bubble_radius):
				self.min_dist_grid(list_of_grids, self.Bubble_initial_pos) 
				self.Bubble_vel = [0, 0]
				Set.add(self)
				return True

		return False


	
	def make_grid(self):
		"""
		make grid returns the positions of each possible bubble placement on the grid
		the odd rows are shifted 
		"""

		init_grid = (self.grid_width//2, self.grid_height//2)
		grid_list = []

		for i in range(self.canv_width//self.grid_width):
			for j in range(self.canv_height//self.grid_height):
				if j == 0 or j%2 ==0:
					grid_list.append((init_grid[0]+i*self.grid_width, init_grid[1]+j*self.grid_height))
					
				else:
					grid_list.append((grid_list[-1][0]+(self.grid_width//2), init_grid[1]+j*self.grid_height))

		return grid_list



	def min_dist_grid(self, list_of_grids, self_pos):
		"""
		finding the closest position in the grid to the center of the bubble after hitting boundary or another bubble
		"""
		
		distance = []
		cp_list_of_grids = list(list_of_grids)
		

		for grid in cp_list_of_grids:
			distance.append((dist(grid, self_pos), cp_list_of_grids.index(grid)))
		grid_point = min(distance)
		idx = grid_point[1]
		point = cp_list_of_grids[idx]
     	
  		self_pos[0] = point[0]
  		self_pos[1] = point[1]

  		self.Bubble_last_pos = [point[0], point[1]]



  	def last_position(self):

  		return self.Bubble_last_pos

     	
  	
	
	def build_adj_dict(self, Set):
		"""
		this function takes a set parameter which includes all the bubbles already shooted and check against 
		tne new bubble for adjacency, if this is the case. it puts the adjacent bubble inside the adjacency dictionary 
		"""
  		if len(Set):

  			for bubble in Set:	
  				
  				distance = dist(bubble.Bubble_last_pos, self.Bubble_last_pos)
  				if  distance <= (bubble.Bubble_radius * 1.2 + self.Bubble_radius * 1.2):
  					# add edge between new bubble and existing bubble
  					if bubble.color not in self.adj_dict.keys():
						self.adj_dict.setdefault(bubble.color,[]).append(bubble)
					else:
						if bubble not in self.adj_dict[bubble.color]:
							self.adj_dict[bubble.color].append(bubble)

					
					if self.color not in bubble.adj_dict.keys(): 
						bubble.adj_dict.setdefault(self.color,[]).append(self)
					else:
						if self not in bubble.adj_dict[self.color]:
							bubble.adj_dict[self.color].append(self)
					
		
		return self.adj_dict


	def get_bubble_chain(self, same_color_chain_list):
		"""
		after shooting the current bubble we need to check the same color chain list and basically do a DFS
		chdecking the adjacent dictionary of the current bubble and go through all the neighbors and make a list 
		of the neighbors with the same color(DFS). (note: it is recursively called on the neighbors of the adjacent neighbor)
		"""

		if self.color in self.adj_dict.keys():
			for bubble in self.adj_dict[self.color]:
				if bubble not in same_color_chain_list:
					same_color_chain_list.append(bubble) 
					bubble.get_bubble_chain(same_color_chain_list)
		return same_color_chain_list



	def bubble_chain_delete(self, same_color_chain_list):
		"""
		iterating through adjacent dictioanry of the bubble and if the adjacent bubble is in the 
		same color chain list we remove the adjacent bubble from adjacent dictionary and continue the process 
		recursively.
		"""

		for bubble in self.adj_dict[self.color]:
			if bubble in same_color_chain_list:
				self.adj_dict[self.color].remove(bubble)
				bubble.bubble_chain_delete(same_color_chain_list)

		del same_color_chain_list[:]
	





