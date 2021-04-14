def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()  # replace a white space
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):  # compare the two strings
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    anagram('dog', 'God ')
