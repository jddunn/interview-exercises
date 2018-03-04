# Sentence-length anagram checker

class Stack():

    def __init__(self, items=[]):
        self.items = items

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


class StripText():

    def strip(self, str_text):
        """Strips text of punctuation marks."""
        punct_chars = [' ', '.', ',', '!', '?', '&', '"', "'", '-', ':']
        str_text = [i for i in str_text if i not in punct_chars]
        str_text = ''.join(str_text)
        return str_text


class AnagramChecker():

    def check_anagram_with_sort(self, str1, str2):
        """Checks if two strings are anagrams with built-in sort."""
        str1 = str1.lower()
        str2 = str2.lower()
        str1 = list(str1)
        str1.sort()
        str2 = list(str2)
        str2.sort()
        str1 = StripText.strip(self, str1)
        str2 = StripText.strip(self, str2)
        pos = 0
        same_chars = True
        while pos < len(str1) and same_chars is True:
            if str1[pos] == str2[pos]:
                pos += 1
            else:
                same_chars = False
        return same_chars

    def check_anagram(self, str1, str2):
        """Checks if two strings are anagrams using a stack (quadratic time)."""
        str1 = StripText.strip(self, str1).lower()
        str1 = [i for i in str1]
        str2 = StripText.strip(self, str2).lower()
        str2 = [i for i in str2]
        chars_holder = Stack()
        index = 0
        for i in str1:
            if chars_holder.is_empty():
                chars_holder.push(i)
                for j in str2:
                    stored_char = chars_holder.peek()
                    if  j == stored_char:
                        chars_holder.pop()
                        break
        if chars_holder.is_empty():
            return True
        else:
            return False


import unittest

class AnagramTest(unittest.TestCase):

    def test_anagram_with_punct_using_sort(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams: ", "I am Lord Voldemort!!", "and",  "Tom Marvolo Riddle", "using built-in sort.")
        self.assertTrue(anagram_checker.check_anagram_with_sort("I am Lord Voldemort!!", "Tom Marvolo Riddle"))

    def test_anagram_using_sort(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams: ", "Florida", "and",  "Rid Of Al", "using built-in sort.")
        self.assertTrue(anagram_checker.check_anagram_with_sort("Florida", "Rid Of Al"))

    def test_anagram_using_stack(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams: ", "Salvages", "and",  "Las Vegas", "using stack object.")
        self.assertTrue(anagram_checker.check_anagram("Salvages", "Las Vegas"))

if __name__ == '__main__':
    unittest.main()