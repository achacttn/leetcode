import unittest

def append_num_five(lst):
    lst.append(5)
    return lst

class TestFunc(unittest.TestCase):
    def test_function_is_appending(self):
        self.assertEqual(append_num_five([1,2,3]), [1,2,3,5])

unittest.main()