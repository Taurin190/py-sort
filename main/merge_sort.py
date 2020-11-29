def merge(list1, list2):
    merged_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    if len(list1) == 0:
        merged_list = merged_list + list2
    else:
        merged_list = merged_list + list1
    return merged_list


def merge_sort(num_list):
    length = len(num_list)
    if length == 1:
        return num_list
    list1 = merge_sort(num_list[0: int(length / 2)])
    list2 = merge_sort(num_list[int(length / 2): length])
    return merge(list1, list2)


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(merge_sort(numbers))
