"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other 
and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
import unittest

def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

class TestStringMethods(unittest.TestCase):
    def test_unique_in_order_uppercase(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])

    def test_unique_in_order_min(self):
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_unique_in_order_number(self):
        self.assertEqual(unique_in_order([1,2,2,3,3]), [1,2,3])

if __name__ == '__main__':
    unittest.main()