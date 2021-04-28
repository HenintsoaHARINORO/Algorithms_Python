memo = {}
def sum_func(n):
    if n <10:
        return n
    if not n in memo:
        num= n %10
        num1= n//10
        memo[n]=num+sum_func(num1)
    return memo[n]
print(sum_func(20))