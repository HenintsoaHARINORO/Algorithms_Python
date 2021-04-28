class Memorize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k - 1)


factorial = Memorize(factorial)
print(factorial(4))  ## to run this code use python RecursionMemorize.py
