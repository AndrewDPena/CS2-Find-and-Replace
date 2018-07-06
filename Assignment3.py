import unittest

'''
Write a recursive method that takes 1) a string to find, 2) a string to replace the found string with, and 3) an initial string. Return the initial string with all the found strings replaced with the replacement string. You may not use loops or the built-in string methods except comparison, length, and slicing. Here is an outline.
'''

'''
Description:
Author: Andrew Peña
Version: 1
Help received from: (people, URLs, etc.)
Help provided to: Raghav Singh
'''

def findandreplace(find, replace, string):
    if find is None or find is "" or replace is None or string is None:
        return string

    if string == "":
       return string

    if find[0] != string[0]:
        return string[0] + findandreplace(find, replace, string[1:])

    if find[0] == string[0]:
        if find == string[:len(find)]:
            return replace + findandreplace(find, replace, string[len(find):])
        else:
            return string[0] + findandreplace(find, replace, string[1:])


class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        self.assertEqual(findandreplace(None, None, None), None)

    def test_find_none(self):
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

    def test_find_empty(self):
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

    def test_replace_none(self):
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

    def test_string_none(self):
        self.assertEqual(findandreplace("a", "b", None), None)

    def test_simple(self):
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

    def test_remove(self):
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

    def test_gettysburg(self):
        self.assertEqual(findandreplace("Four score", "Twenty",
                                        "Four score and seven years ago"), "Twenty and seven years ago")

    def test_scattered_replace(self):
        self.assertEqual(findandreplace("dog", "cat", "My dog is dope. I think dogs are the best animals. I love dogs."),
                         "My cat is dope. I think cats are the best animals. I love cats.")


if __name__ == '__main__':
    unittest.main()
