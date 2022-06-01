import unittest
from events import even_number_of_evens

class TestEvents(unittest.TestCase):
    def test_throws_error_of_value_passed_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)


    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()