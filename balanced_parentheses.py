def balance_check(s):
    if len(s) % 2 != 0 : # check if odd number
        return False
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []

    for parentheses in s:
        if parentheses in opening:
            stack.append(parentheses)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, parentheses) not in matches:
                return False

    return len(stack) == 0
if __name__=="__main__":
    s =balance_check('()')
    print(s)