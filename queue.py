# Basic queue implementation without using insert or append

class Queue():

    def __init__(self, items):
        self.items = items

    def dequeue(self):
        top_item = self.items[0]
        self.items = self.items[-1:]
        return top_item

    def enqueue(self, val_to_insert):
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
        q = Queue([1,2,3,4])
        print("Testing queue enqueue function: " + str(q) + ".")
        self.assertEqual(q.enqueue(0), [0,1,2,3,4])
        print("Result: " + str(q))

    def test_pop(self):
        q = Queue([1,2,3,4])
        print("Testing queue dequeue function: " + str(q) + ".")
        self.assertEqual(q.dequeue(), 1)
        print("Result: "+ str(q))


if __name__ == '__main__':
    unittest.main()