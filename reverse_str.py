# Reverses a string

class Stack():

    def __init__(self, items):
        self.items = items

    def __str__(self):
    	return(''.join(self.items))

    def size(self):
        return len(self.items)

    def is_empty(self):
        return(self.items == [])

    def peek(self):
        return self.items[len(self.items)-1]

    def pop(self):
        top = self.items[len(self.items)-1]
        self.items = self.items[:-1]
        return top

    def push(self, val):
        self.items.append(val)
        return self.items


class ReverseStr():

	def reverse_with_list(self, text):
		temp_str = [0] * len(text)
		last_pos = len(text) - 1
		pos = 0
		for each in text:
			temp_str[pos] = text[last_pos]
			pos += 1
			last_pos -= 1
		self.text = ''.join(temp_str)
		return self.text

	def reverse_with_stack(self, text):
		char_stack = Stack([])
		for each in text:
			char_stack.push(each)
		reverse_stack = Stack([])
		for each in text:
			reverse_stack.push(char_stack.pop())
		return str(reverse_stack)


import unittest

class ReverseStrTest(unittest.TestCase):

	def test_reverse_with_stack(self):
		reverse_str = ReverseStr()
		print("Testing string reversed (with stack): ", "hey there", " - ", "ereht yeh")
		self.assertEqual(reverse_str.reverse_with_stack("hey there"), "ereht yeh")

	def test_reverse_with_list(self):
		reverse_str = ReverseStr()
		print("Testing string reversed (with list): ", "hey there", " - ", "ereht yeh")
		self.assertEqual(reverse_str.reverse_with_list("hey there"), "ereht yeh")

if __name__ == '__main__':
	unittest.main()