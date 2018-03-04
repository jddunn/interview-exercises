# Sentence-length palindrome checker

class StripText():

    def strip(self, str_text):
        punct_chars = [' ', '.', ',', '!', '?', '&', '"', "'", '-', ':']
        str_text = [i for i in str_text if i not in punct_chars]
        str_text = ''.join(str_text)
        return str_text
        

class ReverseStr():

    def reverse(self, str_text):
        temp_str = [0] * len(str_text)
        last_pos = len(str_text) - 1
        pos = 0
        for each in str_text:
            temp_str[pos] = str_text[last_pos]
            pos += 1
            last_pos -= 1
        str_text = ''.join(temp_str)
        return str_text


class PalindromeChecker():

    def is_palindrome_recursive(self, str_text):
        str_text = StripText().strip(str_text.lower())
        if len(str_text) < 1:
            return True
        else:
            if str_text[0] == str_text[-1]:
                return self.is_palindrome_recursive(str_text[1:-1])
            else:
                return False

    def is_palindrome(self, str_text):
        str_text = str_text.lower()
        str_text = StripText().strip(str_text)
        reverse_str = ReverseStr().reverse(str_text)
        if reverse_str == str_text:
            return True
        else:
            return False


import unittest

class PalindromeTest(unittest.TestCase):

    def test_palindrome_with(self):
        palindrome_checker = PalindromeChecker()
        print("Testing palindrome with reverse string equality: ", """Do Geese See God?""")
        self.assertTrue(palindrome_checker.is_palindrome("Do Geese See God?"))

    def test_palindrome_with_recursion(self):
        palindrome_checker = PalindromeChecker()
        print("Testing palindrome with recursion: ", "Do Geese See God?")
        self.assertTrue(palindrome_checker.is_palindrome_recursive("Do Geese See God?"))

    # def test_p

if __name__ == '__main__':
    unittest.main()