numbers = input().split()

length = len(numbers)

for i in range(length - 1):
    for j in range(length - 1):
        if int(numbers[j]) > int(numbers[j + 1]):
            tmp_number = numbers[j + 1]
            numbers[j + 1] = numbers[j]
            numbers[j] = tmp_number
print(numbers)
