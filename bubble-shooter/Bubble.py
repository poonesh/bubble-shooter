
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
		self.Bubble_radius = 15
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
		


		self.Bubble_index = self.tk_pic.create_oval(self.x0, self.y0, self.x1 , self.y1, outline = "grey", fill = self.color, width = 2)                                        
		self.tk_pic.shapesBubble[self.Bubble_index] = self


	
	# calculating velocity in the updated direction 
	def fire_Bubble(self, vel, firing_angle):

		vec = ang_to_vec(firing_angle)
		self.Bubble_vel = [vel*vec[0], vel*vec[1]]

	
	
	
	def update_Bubble(self):
		
		self.Bubble_initial_pos[0] += self.Bubble_vel[0]
		self.Bubble_initial_pos[1] += self.Bubble_vel[1]

		self.x0 = self.Bubble_initial_pos[0] - self.Bubble_radius
		self.y0 = self.Bubble_initial_pos[1] - self.Bubble_radius
		self.x1 = self.Bubble_initial_pos[0] + self.Bubble_radius
		self.y1 = self.Bubble_initial_pos[1] + self.Bubble_radius 

		self.tk_pic.coords(self.Bubble_index, self.x0, self.y0, self.x1, self.y1)




	def check_boundary(self):

		if self.Bubble_initial_pos[0] <= self.Bubble_radius or self.Bubble_initial_pos[0] >= self.tk_pic.width - self.Bubble_radius:
			self.Bubble_vel[0] = -self.Bubble_vel[0]


	
	

	def is_stuck(self, Set, list_of_grids):
	
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

  		if len(Set):

  			for bubble in Set:	
  				
  				distance = dist(bubble.Bubble_last_pos, self.Bubble_last_pos)
  				if  distance <= (bubble.Bubble_radius + self.Bubble_radius):
  					
  					if bubble.color not in self.adj_dict:
  						self.adj_dict[bubble.color] = []
					self.adj_dict.setdefault(bubble.color,[]).append(bubble)
					
					if self.color not in bubble.adj_dict: 
						bubble.adj_dict[self.color] = []
					bubble.adj_dict.setdefault(self.color,[]).append(self)
					
		return self.adj_dict



	

	def get_bubble_chain(self, same_color_chain_list):

		if self.color in self.adj_dict.keys():
			for bubble in self.adj_dict[self.color]:
				if bubble not in same_color_chain_list:
					same_color_chain_list.append(bubble) 
					bubble.get_bubble_chain(same_color_chain_list)

		





