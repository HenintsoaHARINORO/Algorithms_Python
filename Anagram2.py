def anagram2(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    #if len(s1) != len(s2):
     #   return False
    count = {}  # dictionary

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    print(count)
    for letter in s2:
        if letter in count:
           count[letter] -= 1
        else:
            count[letter] = 1
    print(count)
    for k in count:
        if count[k] != 0:
          print(False)

    print(True)


if __name__ == '__main__':
    anagram2('cat',"tac")
