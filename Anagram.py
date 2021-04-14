def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()  # replace a white space
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)  # compare the two strings
