memo ={}
def rec_sum(n):
    if n == 0:
        return 0
    if not n in memo:
        memo[n]= n+ rec_sum(n-1)
    return memo[n]

print(rec_sum(5))