from graph.sorting import InsertionSorter, QuickSorter

import unittest
import random


class TestSorters(unittest.TestCase):
    def setUp(self):
        self.test_cases = []
        self.num_test_cases = 10

        # Make an array of testcases
        for i in range(self.num_test_cases):
            case = []
            for i in range(10):
                case.append(random.randrange(1000))

            self.test_cases.append(case)

    def test_insertion(self):
        sorter = InsertionSorter()

        for case in self.test_cases:
            sorter_sorted = sorter.sort(case)[:]

            self.assertEqual(sorter_sorted, sorted(case))

    def test_quicksort(self):
        sorter = QuickSorter()

        for case in self.test_cases:
            sorter_sorted = sorter.sort(case)[:]

            self.assertEqual(sorter_sorted, sorted(case))



if __name__ == '__main__':
    unittest.main()
