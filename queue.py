# Basic queue implementation without using insert or append

class QueueList():

    def __init__(self, items):
        self.items = items

    def pop(self):
        top_item = self.items[0]
        self.items = self.items[-1:]
        return top_item

    def push(self, val_to_insert):
        temp_items=[0]*(len(self.items) + 1)    
        temp_items[0] = val_to_insert
        pos = 1
        for i in range(0, len(self.items)):
            if pos > len(temp_items):
               pass
            else:
                temp_items[pos] = self.items[i]
                pos += 1
        self.items = temp_items
        return self.items

    def __repr__(self):
        pos = 0 
        text_str = ""
        for each in self.items:
            if pos >= len(self.items) - 1:
                text_str += str(each)
            else:
                pos += 1
                text_str += str(each) + ', '
        return text_str


import unittest

class QueueTest(unittest.TestCase):

    def test_push(self):
        li = QueueList([1,2,3,4])
        print("Testing queue push function: " + str(li) + ".")
        self.assertEqual(li.push(0), [0,1,2,3,4])
        print("Result: " + str(li))

    def test_pop(self):
        li = QueueList([1,2,3,4])
        print("Testing queue pop function: " + str(li) + ".")
        self.assertEqual(li.pop(), 1)
        print("Result: "+ str(li))


if __name__ == '__main__':
    unittest.main()