debug_flag = True


def d_print(message):
    if debug_flag:
        print(message)


def partition(num_list, start, end):
    sorted_num_list = num_list
    i = start - 1
    j = end
    pivot = sorted_num_list[end]
    d_print("pivot: " + str(pivot))
    while True:
        i = i + 1
        while sorted_num_list[i] < pivot:
            i = i + 1
        j = j - 1
        while i < j and pivot < sorted_num_list[j]:
            j = j - 1
        if i >= j:
            break
        d_print(str(sorted_num_list[i]) + " <=> " + str(sorted_num_list[j]))
        tmp = sorted_num_list[i]
        sorted_num_list[i] = sorted_num_list[j]
        sorted_num_list[j] = tmp
    d_print(str(sorted_num_list[i]) + " <=> " + str(sorted_num_list[end]))
    tmp = sorted_num_list[i]
    sorted_num_list[i] = sorted_num_list[end]
    sorted_num_list[end] = tmp
    return sorted_num_list, i


def quick_sort(num_list, start, end):
    sorted_num_list = num_list
    if start >= end:
        return sorted_num_list
    sorted_num_list, divider = partition(num_list, start, end)
    d_print(sorted_num_list)
    sorted_num_list = quick_sort(sorted_num_list, start, divider - 1)
    sorted_num_list = quick_sort(sorted_num_list, divider + 1, end)
    return sorted_num_list


numbers = [int(x) for x in input().split()]
length = len(numbers)
print(quick_sort(numbers, 0, length - 1))


