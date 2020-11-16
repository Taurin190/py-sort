numbers = input().split()

length = len(numbers)

for i in range(length):
    tmp_min = None
    for j in range(length - i):
        if not tmp_min:
            tmp_min = numbers[j]
        elif int(tmp_min) > int(numbers[j]):
            tmp_min = numbers[j]
    numbers[i] = tmp_min
print(numbers)
