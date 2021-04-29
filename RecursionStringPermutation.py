def permute(s):
    output = []

    if len(s)==1:
        output = [s]
    else:
        for i , let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                output +=[let+perm]
    return output
print(permute("abc"))