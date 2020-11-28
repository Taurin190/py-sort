numbers = [int(x) for x in input().split()]

length = len(numbers)

sorted_numbers = []

for i in range(length):
    if len(sorted_numbers) == 0:
        sorted_numbers.append(numbers[i])
        continue
    for j in range(len(sorted_numbers)):
        if numbers[i] < sorted_numbers[j]:
            sorted_numbers.insert(j, numbers[i])
            break
        if j == len(sorted_numbers) - 1:
            sorted_numbers.append(numbers[i])
print(sorted_numbers)
