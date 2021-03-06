from unittest import TestCase
from main.quick_sort import quick_sort_main


class TestQuickSort(TestCase):
    def test_sort_1(self):
        numbers = [5, 4, 3, 2, 1]
        sorted_number_list = quick_sort_main(numbers)
        self.assertEqual(sorted_number_list, [1, 2, 3, 4, 5])

    def test_sort_2(self):
        numbers = [5, 10, 3, 7, 8, 1, 6]
        sorted_number_list = quick_sort_main(numbers)
        self.assertEqual(sorted_number_list, [1, 3, 5, 6, 7, 8, 10])
