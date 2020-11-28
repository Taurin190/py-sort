def select_sort(num_list):
    length = len(num_list)
    for i in range(length - 1):
        tmp_min = None
        tmp_min_index = i
        for j in range(i, length):
            if not tmp_min:
                tmp_min = num_list[j]
            elif tmp_min > num_list[j]:
                tmp_min = num_list[j]
                tmp_min_index = j
        num_list[tmp_min_index] = num_list[i]
        num_list[i] = tmp_min
    return num_list


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(select_sort(numbers))
