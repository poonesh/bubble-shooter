
import unittest
from Bubble import Bubble
# from Bubble_Tkinter import TKPICTURE 

from tk_picture_fake import FAKE_TKPICTURE
fake_tk_picture = FAKE_TKPICTURE(600, 600)




class Bubble_Shooter_Test(unittest.TestCase):

	
	def test_build_adj_dict_two__bubbles(self):

		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="yellow")
		bubble_3 = Bubble(fake_tk_picture, color="red")

		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [130, 100]
		bubble_3.Bubble_last_pos = [70, 70]
		
		get_stuck = set([bubble_1])

		result = bubble_2.build_adj_dict(get_stuck)
		expected = {}
		expected[bubble_1.color] = [bubble_1] 
		self.assertEqual(len(result["blue"]), len(expected[bubble_1.color]))
		self.assertTrue(result[(bubble_1.color)][0] is expected[(bubble_1.color)][0])
		self.assertTrue(result[(bubble_1.color)][0] is bubble_1)



	def test_build_adj_dict_three_bubbles(self):
		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="yellow")
		bubble_3 = Bubble(fake_tk_picture, color="red")

		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [100, 130]
		bubble_3.Bubble_last_pos = [130, 130]

		get_stuck = set([bubble_1, bubble_3])
		result = bubble_2.build_adj_dict(get_stuck)
		expected = {}
		expected[bubble_1.color] = [bubble_1]
		expected[bubble_3.color] = [bubble_3]


		self.assertEqual(len(result["blue"]), len(expected[bubble_1.color]))
		self.assertTrue(result[(bubble_1.color)][0] is expected[(bubble_1.color)][0])
		self.assertTrue(result[(bubble_1.color)][0] is bubble_1)

		self.assertEqual(len(result["red"]), len(expected[bubble_3.color]))
		self.assertTrue(result[(bubble_3.color)][0] is expected[(bubble_3.color)][0])
		self.assertTrue(result[(bubble_3.color)][0] is bubble_3)

		self.assertTrue("yellow" not in result)
		


	def test_build_adj_dict_three__bubbles_same_color_adjecent(self):
		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="blue")
		bubble_3 = Bubble(fake_tk_picture, color="blue")

		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [100, 130]
		bubble_3.Bubble_last_pos = [130, 130]

		get_stuck = set([bubble_1, bubble_3])
		result = bubble_2.build_adj_dict(get_stuck)
		expected = {}
		expected[bubble_1.color] = [bubble_1, bubble_3]
		expected[bubble_3.color] = [bubble_1, bubble_3]
		expected[bubble_2.color] = [bubble_1, bubble_3]


		self.assertEqual(len(result["blue"]), len(expected[bubble_3.color]))
		self.assertTrue(result[bubble_1.color][1] is expected[(bubble_1.color)][1])
		self.assertTrue(result[bubble_2.color][1] is expected[(bubble_2.color)][1])
		self.assertTrue(result[bubble_2.color][0] is expected[(bubble_2.color)][0])


		self.assertTrue("yellow" not in result)
		self.assertTrue("blue" in result)

	

	def test_build_adj_dict_three__bubbles_same_color_not_adjecent(self):

		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="blue")
		bubble_3 = Bubble(fake_tk_picture, color="blue")

		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [130, 130]
		bubble_3.Bubble_last_pos = [70, 70]	
	

		get_stuck = set([bubble_1, bubble_3])
		result = bubble_2.build_adj_dict(get_stuck)
		expected = {}
		

		self.assertEqual(len(result), len(expected))
		self.assertTrue("yellow" not in result)



	def test_build_adj_dict_three__bubbles_same_color_3_adjecent(self):

		bubble_1 = Bubble(fake_tk_picture, color="blue")
		bubble_2 = Bubble(fake_tk_picture, color="blue")
		bubble_3 = Bubble(fake_tk_picture, color="blue")

		bubble_1.Bubble_last_pos = [100, 100]
		bubble_2.Bubble_last_pos = [100, 130]
		bubble_3.Bubble_last_pos = [115, 115]	
	

		get_stuck = set([bubble_1, bubble_3])
		result = bubble_2.build_adj_dict(get_stuck)
		expected = {}
		expected[bubble_1.color] = [bubble_2, bubble_3]

		
		self.assertEqual(len(result), len(expected))
		self.assertTrue(result[bubble_1.color][1] is expected[bubble_1.color][1])
		
		
		

if __name__ == '__main__':
	unittest.main()

