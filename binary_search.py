# Binary search for ordered lists

class BinarySearch():

	def binary_search(self, item, items):
		found = False
		first = 0
		last = len(items) - 1
		while first <= last and not found:
			mid = (first + last) // 2
			if item == items[mid]:
				found = True
			if item < items[mid]:
				last = mid - 1
			else:
				first = mid + 1
		return found


import unittest

class BinarySearchTest(unittest.TestCase):

	def test_binary_search(self):
		item = 14
		items = [3, 5, 9, 14, 24, 28, 30, 33, 39, 41, 47, 50, 55, 61, 68, 73, 81, 89, 93, 97, 100]
		print("Testing binary search for", item, "in", items)
		self.assertTrue(BinarySearch().binary_search(item, items))

if __name__ == '__main__':
	unittest.main()