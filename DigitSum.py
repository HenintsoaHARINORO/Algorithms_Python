def sum_func(n):
    if n == 0:
        return 0
    else:
        num= n %10
        num1= n//10
        return  num+sum_func(num1)
print(sum_func(20))