# Selection sort

class SelectionSort():

	def selection_sort(self, items):
		for val in range(len(items)-1, 0, -1):
			max_pos = 0
			for idx in range(1, val+1):
				if items[idx] > items[max_pos]:
					max_pos = idx
			prev_val = items[val]
			items[val] = items[max_pos]
			items[max_pos] = prev_val
		return items


import unittest

class SelectionSortTest(unittest.TestCase):

	def test_selection_sort(self):
		unsorted_items = [0, 14, 24, 5, 9, 7, 16, 3, 11, 1, 20]		
		sorted_items = [0, 1, 3, 5, 7, 9, 11, 14, 16, 20, 24]
		print("Testing selection sort for: ", unsorted_items, "to", sorted_items)
		self.assertEqual(SelectionSort().selection_sort(unsorted_items), sorted_items)

if __name__ == "__main__":
	unittest.main()