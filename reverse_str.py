# Reverses a string

class ReverseStr():

	def reverse(self, str_text):
		temp_str = [0] * len(str_text)
		last_pos = len(str_text) - 1
		pos = 0
		for each in str_text:
			temp_str[pos] = str_text[last_pos]
			pos += 1
			last_pos -= 1
		self.str_text = ''.join(temp_str)
		return self.str_text


import unittest

class ReverseStrTest(unittest.TestCase):

	def test_reverse(self):
		reverse_str = ReverseStr()
		print("Testing string reversed: ", "hey there", " - ", "ereht yeh")
		self.assertEqual(reverse_str.reverse("hey there"), "ereht yeh")

if __name__ == '__main__':
	unittest.main()