import unittest

import techTask as task

class TechTaskTest(unittest.TestCase):

    def test_shouldRaiseAValueErrorWhenPassedANegativeNumber(self):
        with self.assertRaises(ValueError):
            task.primesUpTo(-1)

    def test_shouldReturnAnEmptyListWhenTheSearchSpaceIs0to0(self):
        self.assertEqual(task.primesUpTo(0), [])

    def test_shouldReturnAnEmptyListWhenTheSearchSpaceIs0to1(self):
        self.assertEqual(task.primesUpTo(1), [])

    def test_shouldReturnAnEmptyListWhenTheSearchSpaceIs0to2(self):
        self.assertEqual(task.primesUpTo(2), [])

    def test_shouldAListWithTheOnlyPrimeWhenTheSearchSpaceIs0to3(self):
        self.assertEqual(task.primesUpTo(3), [2])

    def test_shouldAListWithTwoPrimesWhenTheSearchSpaceIs0to4(self):
        self.assertEqual(task.primesUpTo(4), [2, 3])

    def test_shouldAListWithAllThePrimesWhenTheSearchSpaceIs0to20(self):
        self.assertEqual(task.primesUpTo(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_shouldAListWithAllThePrimesWhenTheSearchSpaceIs0to40(self):
        self.assertEqual(task.primesUpTo(40), [2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37])



if __name__ == '__main__':
    unittest.main()
