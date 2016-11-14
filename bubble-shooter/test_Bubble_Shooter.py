
import unittest
from Bubble import Bubble
# from Bubble_Tkinter import TKPICTURE 

from tk_picture_fake import FAKE_TKPICTURE
fake_tk_picture = FAKE_TKPICTURE(600, 600)




class Bubble_Shooter_Test(unittest.TestCase):

	
	# def test_build_adj_dict_two__bubbles(self):

	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="yellow")
	# 	bubble_3 = Bubble(fake_tk_picture, color="red")

	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [130, 100]
	# 	bubble_3.Bubble_last_pos = [70, 70]
		
	# 	get_stuck = set([bubble_1])

	# 	result = bubble_2.build_adj_dict(get_stuck)
	# 	expected = {}
	# 	expected[bubble_1.color] = [bubble_1] 
	# 	self.assertEqual(len(result["blue"]), len(expected[bubble_1.color]))
	# 	self.assertTrue(result[(bubble_1.color)][0] is expected[(bubble_1.color)][0])
	# 	self.assertTrue(result[(bubble_1.color)][0] is bubble_1)



	# def test_build_adj_dict_three_bubbles(self):
	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="yellow")
	# 	bubble_3 = Bubble(fake_tk_picture, color="red")

	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [100, 130]
	# 	bubble_3.Bubble_last_pos = [130, 130]

	# 	get_stuck = set([bubble_1, bubble_3])
	# 	result = bubble_2.build_adj_dict(get_stuck)
	# 	expected = {}
	# 	expected[bubble_1.color] = [bubble_1]
	# 	expected[bubble_3.color] = [bubble_3]


	# 	self.assertEqual(len(result["blue"]), len(expected[bubble_1.color]))
	# 	self.assertTrue(result[(bubble_1.color)][0] is expected[(bubble_1.color)][0])
	# 	self.assertTrue(result[(bubble_1.color)][0] is bubble_1)

	# 	self.assertEqual(len(result["red"]), len(expected[bubble_3.color]))
	# 	self.assertTrue(result[(bubble_3.color)][0] is expected[(bubble_3.color)][0])
	# 	self.assertTrue(result[(bubble_3.color)][0] is bubble_3)

	# 	self.assertTrue("yellow" not in result)
		


	# def test_build_adj_dict_three__bubbles_same_color_adjecent(self):
	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_3 = Bubble(fake_tk_picture, color="blue")

	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [100, 130]
	# 	bubble_3.Bubble_last_pos = [130, 130]

	# 	get_stuck = set([bubble_1, bubble_3])
	# 	result = bubble_2.build_adj_dict(get_stuck)
	# 	expected = {}
	# 	expected[bubble_1.color] = [bubble_1, bubble_3]
	# 	expected[bubble_3.color] = [bubble_1, bubble_3]
	# 	expected[bubble_2.color] = [bubble_1, bubble_3]


	# 	self.assertEqual(len(result["blue"]), len(expected[bubble_3.color]))
	# 	self.assertTrue(result[bubble_1.color][1] is expected[(bubble_1.color)][1])
	# 	self.assertTrue(result[bubble_2.color][1] is expected[(bubble_2.color)][1])
	# 	self.assertTrue(result[bubble_2.color][0] is expected[(bubble_2.color)][0])


	# 	self.assertTrue("yellow" not in result)
	# 	self.assertTrue("blue" in result)

	

	# def test_build_adj_dict_three__bubbles_same_color_not_adjecent(self):

	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_3 = Bubble(fake_tk_picture, color="blue")

	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [130, 130]
	# 	bubble_3.Bubble_last_pos = [70, 70]	
	

	# 	get_stuck = set([bubble_1, bubble_3])
	# 	result = bubble_2.build_adj_dict(get_stuck)
	# 	expected = {}
		

	# 	self.assertEqual(len(result), len(expected))
		



	# def test_build_adj_dict_three__bubbles_same_color_3_adjecent(self):

	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_3 = Bubble(fake_tk_picture, color="blue")

	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [100, 130]
	# 	bubble_3.Bubble_last_pos = [115, 115]	
	

	# 	get_stuck = set([bubble_1, bubble_3])
	# 	result = bubble_2.build_adj_dict(get_stuck)
	# 	expected = {}
	# 	expected[bubble_1.color] = [bubble_2, bubble_3]

		
	# 	self.assertEqual(len(result), len(expected))
	# 	self.assertTrue(result[bubble_1.color][1] is expected[bubble_1.color][1])




	# def test_get_bubble_chain_2adjacent_blue_one_red(self):

	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_3 = Bubble(fake_tk_picture, color="red")


	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [100, 130]
	# 	bubble_3.Bubble_last_pos = [100, 160]

	# 	get_stuck = set([bubble_2, bubble_3])

	# 	bubble_1.adj_dict = bubble_1.build_adj_dict(get_stuck)
	# 	print type(bubble_1.adj_dict)
	# 	print bubble_1.adj_dict


	# 	same_color_chain_list = []
	# 	bubble_1.get_bubble_chain(same_color_chain_list)
	# 	print "same_color_chain_list", same_color_chain_list
		

	# 	expected = [bubble_1, bubble_2]
	# 	self.assertEqual(len(expected), len(same_color_chain_list))
	# 	self.assertTrue(expected[0] is same_color_chain_list[1])
	# 	print expected[1]
	# 	print same_color_chain_list[0]

	# 	print expected[0]
	# 	print same_color_chain_list[1]



	# def test_get_bubble_chain_3adjacent_blue(self):

	# 	bubble_1 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_2 = Bubble(fake_tk_picture, color="blue")
	# 	bubble_3 = Bubble(fake_tk_picture, color="red")
	#   	bubble_4 = Bubble(fake_tk_picture, color="red")


	# 	bubble_1.Bubble_last_pos = [100, 100]
	# 	bubble_2.Bubble_last_pos = [100, 130]
	# 	bubble_3.Bubble_last_pos = [130, 130]
	# 	bubble_4.Bubble_last_pos = [130, 100]
		

	# 	get_stuck = set([bubble_2, bubble_3, bubble_4])
	# 	bubble_1.adj_dict = bubble_1.build_adj_dict(get_stuck)
		
	# 	get_stuck_1 = set([bubble_1, bubble_3, bubble_4])
	# 	bubble_2.adj_dict = bubble_2.build_adj_dict(get_stuck_1)

	# 	get_stuck_2 = set([bubble_1, bubble_2, bubble_4])
	# 	bubble_3.adj_dict = bubble_3.build_adj_dict(get_stuck_2)

	# 	get_stuck_3 = set([bubble_1, bubble_2, bubble_3])
	# 	bubble_4.adj_dict = bubble_4.build_adj_dict(get_stuck_3)


	# 	same_color_chain_list = []
	# 	bubble_1.get_bubble_chain(same_color_chain_list)
	# 	print "same_color_chain_list", same_color_chain_list

	# 	expected = [bubble_1, bubble_2]
	# 	print "bubble_1", bubble_1
	# 	print "bubble_2", bubble_2


	# 	self.assertEqual(len(expected), len(same_color_chain_list))
	# 	print "expected", expected
	# 	print "same_color_chain_list", same_color_chain_list




	def test_bubble_chain_delete(self):

		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="blue")
		bubble_3 = Bubble(fake_tk_picture, color="blue")
	  	bubble_4 = Bubble(fake_tk_picture, color="red")


		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [100, 130]
		bubble_3.Bubble_last_pos = [130, 130]
		bubble_4.Bubble_last_pos = [130, 100]
		

		get_stuck = set([bubble_2, bubble_3, bubble_4])
		bubble_1.adj_dict = bubble_1.build_adj_dict(get_stuck)
		print "bubble_1_dict_1", bubble_1.adj_dict
		
		get_stuck_1 = set([bubble_1, bubble_3, bubble_4])
		bubble_2.adj_dict = bubble_2.build_adj_dict(get_stuck_1)
		print "bubble_1_dict_2", bubble_2.adj_dict
		# print "bubble_2_dict", bubble_2.adj_dict

		get_stuck_2 = set([bubble_1, bubble_2, bubble_4])
		bubble_3.adj_dict = bubble_3.build_adj_dict(get_stuck_2)
		print "bubble_3_dict", bubble_3.adj_dict

		get_stuck_3 = set([bubble_1, bubble_2, bubble_3])
		bubble_4.adj_dict = bubble_4.build_adj_dict(get_stuck_3)
		print "bubble_4_dict", bubble_4.adj_dict


		same_color_chain_list = []
		bubble_3.get_bubble_chain(same_color_chain_list)
		

		bubble_3.bubble_chain_delete(same_color_chain_list)
		expected = {'blue':[], 'red':[bubble_4]}

		print "expected", expected
		print "bubble_3.adj_dict", bubble_3.adj_dict
		

		self.assertEqual(expected['blue'], bubble_3.adj_dict['blue'])
		self.assertEqual(expected['red'], bubble_3.adj_dict['red'])
		self.assertEqual(expected, bubble_3.adj_dict)





if __name__ == '__main__':
	unittest.main()

