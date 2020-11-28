def insert_sort(number_list):
    length = len(number_list)
    sorted_numbers = []
    for i in range(length):
        if len(sorted_numbers) == 0:
            sorted_numbers.append(number_list[i])
            continue
        for j in range(len(sorted_numbers)):
            if number_list[i] < sorted_numbers[j]:
                sorted_numbers.insert(j, number_list[i])
                break
            if j == len(sorted_numbers) - 1:
                sorted_numbers.append(number_list[i])
    return sorted_numbers


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    print(insert_sort(numbers))
