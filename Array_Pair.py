def pair_sum(arr, k):
    if len(arr) < 2:
        return
    # Sets for tracking
    seen = set()
    output = set()
    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))
    # return  print(len(output))
    print('\n'.join(map(str, list(output))))  # convert into string and join then
    print(seen)


if __name__ == '__main__':
    pair_sum([1, 3, 2, 2], 4)
