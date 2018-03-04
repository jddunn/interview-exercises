# Sentence-length anagram checker with three implementations

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

    def check_anagram_with_dict(self, str1, str2):
        """Checks if two strings are anagrams by storing and checking char counts in dictionaries (linear time)."""
        str1 = str1.lower()
        str2 = str2.lower()
        str1 = StripText.strip(self, str1)
        str2 = StripText.strip(self, str2)
        str1_count = {}
        str2_count = {}
        for each in str1:
            try:
                if str1_count[each]:
                    str1_count[each] += 1
            except:
                str1_count[each] = 1
        for each in str2:
            try:
                if str2_count[each]:
                    str2_count[each] += 1
            except:
                str2_count[each] = 1
        for each in str1_count:
            if str1_count[each] == str2_count[each]:
                pass
            else:
                return False
        return True

    def check_anagram_with_sort(self, str1, str2):
        """Checks if two strings are anagrams with built-in sort (linear time)."""
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
import time

class AnagramTest(unittest.TestCase):

    print("Testing anagrams: ", "THIS TEXT AND THE ONE BESIDE IT ARE EQUAL. I WROTE THIS ONE FIRST, AND THEN I GAVE IT TO MY FRIEND CHRISTIAN BOK AND ASKED HIM TO GENERATE A NEW TEXT USING EVERY LETTER AND EVERY PUNCTUATION MARK THAT I USED IN MINE. THE OTHER TEXT IS HIS." "MICAH LEXIER REQUESTED IN ADVANCE THAT I REINVENT HIS TEXT. SO I UNKNOTTED IT AND REKNITTED IT INTO THIS VERY FORM, BUT THEN I BEGAN TO THINK THAT HIS MESSAGE HAD ALREADY RESEWN A TOUTED ART OF GENUINE POETRY. HIS EERIE TEXT WAS MINE.")

    def test_anagram_using_dict(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams using dictionaries.")
        start = time.time() * 1000
        self.assertTrue(anagram_checker.check_anagram_with_dict("THIS TEXT AND THE ONE BESIDE IT ARE EQUAL. I WROTE THIS ONE FIRST, AND THEN I GAVE IT TO MY FRIEND CHRISTIAN BOK AND ASKED HIM TO GENERATE A NEW TEXT USING EVERY LETTER AND EVERY PUNCTUATION MARK THAT I USED IN MINE. THE OTHER TEXT IS HIS.", "MICAH LEXIER REQUESTED IN ADVANCE THAT I REINVENT HIS TEXT. SO I UNKNOTTED IT AND REKNITTED IT INTO THIS VERY FORM, BUT THEN I BEGAN TO THINK THAT HIS MESSAGE HAD ALREADY RESEWN A TOUTED ART OF GENUINE POETRY. HIS EERIE TEXT WAS MINE."))
        end = time.time() * 1000
        duration = end - start
        print("Processing duration: " + str(duration) +" milliseconds.")

    def test_anagram_using_sort(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams using built-in sort.")
        start = time.time() * 1000
        self.assertTrue(anagram_checker.check_anagram_with_sort("THIS TEXT AND THE ONE BESIDE IT ARE EQUAL. I WROTE THIS ONE FIRST, AND THEN I GAVE IT TO MY FRIEND CHRISTIAN BOK AND ASKED HIM TO GENERATE A NEW TEXT USING EVERY LETTER AND EVERY PUNCTUATION MARK THAT I USED IN MINE. THE OTHER TEXT IS HIS.", "MICAH LEXIER REQUESTED IN ADVANCE THAT I REINVENT HIS TEXT. SO I UNKNOTTED IT AND REKNITTED IT INTO THIS VERY FORM, BUT THEN I BEGAN TO THINK THAT HIS MESSAGE HAD ALREADY RESEWN A TOUTED ART OF GENUINE POETRY. HIS EERIE TEXT WAS MINE."))
        end = time.time() * 1000
        duration = end - start
        print("Processing duration: " + str(duration) +" milliseconds.")

    def test_anagram_using_stack(self):
        anagram_checker = AnagramChecker()
        print("Testing anagrams using stack object.")
        start = time.time() * 1000
        self.assertTrue(anagram_checker.check_anagram("THIS TEXT AND THE ONE BESIDE IT ARE EQUAL. I WROTE THIS ONE FIRST, AND THEN I GAVE IT TO MY FRIEND CHRISTIAN BOK AND ASKED HIM TO GENERATE A NEW TEXT USING EVERY LETTER AND EVERY PUNCTUATION MARK THAT I USED IN MINE. THE OTHER TEXT IS HIS.", "MICAH LEXIER REQUESTED IN ADVANCE THAT I REINVENT HIS TEXT. SO I UNKNOTTED IT AND REKNITTED IT INTO THIS VERY FORM, BUT THEN I BEGAN TO THINK THAT HIS MESSAGE HAD ALREADY RESEWN A TOUTED ART OF GENUINE POETRY. HIS EERIE TEXT WAS MINE."))
        end = time.time() * 1000
        duration = end - start
        print("Processing duration: " + str(duration) +" milliseconds.")

if __name__ == '__main__':
    unittest.main()