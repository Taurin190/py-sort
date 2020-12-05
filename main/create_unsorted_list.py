import random


def get_unsorted_list(max, length):
    original_list = list(range(max))
    unsorted_list = []
    while len(unsorted_list) < length:
        index = random.randint(0, len(original_list) - 1)
        unsorted_list.append(original_list.pop(index))
    return unsorted_list


if __name__ == '__main__':
    print(get_unsorted_list(20, 10))