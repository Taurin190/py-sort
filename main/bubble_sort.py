def bubble_sort(number_list):
    length = len(number_list)
    for i in range(length - 1):
        for j in range(length - 1):
            if number_list[j] > number_list[j + 1]:
                tmp_number = number_list[j + 1]
                number_list[j + 1] = number_list[j]
                number_list[j] = tmp_number
    return number_list


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(bubble_sort(numbers))
