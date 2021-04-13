numbers = [10, 200, 30, 40, 50]

# random indexity -->O(1) get items if we know the index
# print(numbers[0])
# numbers[1]=200

# for num in numbers:
# print(num)

# for i in range(len(numbers)):
#   print(numbers[i])

print(numbers[0:3])
print(numbers[:-2])  # print all items except the last two

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)
