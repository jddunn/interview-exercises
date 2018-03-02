# Sentence-length anagram checker

class StripText():

    def strip(self, str_text):
        str_removed_punct = []
        for each in list(str_text):
            if (each != ' '  and each != '.' and each != '!' and each != '&' and each != '"' and 
                  each != "'" and each != '?' and each != ',' and each != '-' and each != ':'):
                str_removed_punct.append(each)
        str_text = ''.join(str_removed_punct)
        return str_text


class AnagramChecker():

	def check_anagram(self, str1, str2):
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


import unittest

class AnagramTest(unittest.TestCase):

	def test_anagram(self):
		anagram_checker = AnagramChecker()
		print("Testing anagrams: ", "Florida", "and",  "Rid Of Al")
		self.assertTrue(anagram_checker.check_anagram("Florida", "Rid Of Al"))

	def test_anagram_with_punct(self):
		anagram_checker = AnagramChecker()
		print("Testing anagrams: ", "I am Lord Voldemort!!", "and",  "Tom Marvolo Riddle")
		self.assertTrue(anagram_checker.check_anagram("I am Lord Voldemort!!", "Tom Marvolo Riddle"))

if __name__ == '__main__':
	unittest.main()