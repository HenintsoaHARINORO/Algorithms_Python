memo = {}
def sum_func(n):
    if n == 0:
        return 0
    if not n in memo:
        num= n %10
        num1= n//10
        memo[n]=num+sum_func(num1)
    return memo[n]
print(sum_func(20))