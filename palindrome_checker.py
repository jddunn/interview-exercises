# Sentence-length palindrome checker

class StripText():

    def strip(self, str_text):
        str_removed_punct = []
        for each in list(str_text):
            if (each != ' '  and each != '.' and each != '!' and each != '&' and each != '"' and 
                  each != "'" and each != '?' and each != ',' and each != '-' and each != ':'):
                str_removed_punct.append(each)
        str_text = ''.join(str_removed_punct)
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

    def test_palindrome(self):
        palindrome_checker = PalindromeChecker()
        print("Testing palindrome: ", "anna")
        self.assertTrue(palindrome_checker.is_palindrome("anna"))

    def test_palindrome_with_punct(self):
        palindrome_checker = PalindromeChecker()
        print("Testing palindrome sentence: ", "Do Geese See God?")
        self.assertTrue(palindrome_checker.is_palindrome("Do Geese See God?"))


if __name__ == '__main__':
    unittest.main()