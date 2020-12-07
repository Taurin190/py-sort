from main.bubble_sort import bubble_sort
from main.insert_sort import insert_sort
from main.merge_sort import merge_sort
from main.quick_sort import quick_sort_main as quick_sort
from main.select_sort import select_sort
from main.create_unsorted_list import get_unsorted_list

import time


def benchmark(function_name, unsorted_list):
    print(function_name)
    start = time.time()
    print(eval(function_name)(unsorted_list))
    print("Time: " + str(time.time() - start))


if __name__ == '__main__':
    unsorted_list = get_unsorted_list(3000, 2000)
    benchmark("bubble_sort", unsorted_list)
    benchmark("insert_sort", unsorted_list)
    benchmark("merge_sort", unsorted_list)
    benchmark("quick_sort", unsorted_list)
    benchmark("select_sort", unsorted_list)