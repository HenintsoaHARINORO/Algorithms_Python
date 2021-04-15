def rev_word(s):
    words = []  # a list
    length = len(s)
    space = [' ']
    i = 0
    while i < length:
        if s[i] not in space:
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
        i += 1
    print(" ".join(reversed(words)))


if __name__ == '__main__':
    rev_word("How are you  Henintsoa")
