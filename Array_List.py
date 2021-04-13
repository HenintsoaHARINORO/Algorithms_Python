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

# O(n) time complexity
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

#Hacker rank
for i in range(5):
    if i < 5 and i >= 0:
        print(i * i)

for i in range(4):
    if i != 0:
        print(i, end="")

firstname = "Henintsoa"
last = "Randria"
print("Hello " + firstname + " " + last)
