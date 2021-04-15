def uni_char(s):
    print(len(set(s)) == len(s))  # set takes all unique characters


def uni_char2(s):
    char = set()
    for letter in s:  # checking if it already exist in the set
        if letter in char:
            print(False)
        else:
            char.add(letter)
    print(True)


if __name__ == '__main__':
    uni_char('abdcfa')
