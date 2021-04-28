def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]


print(reverse("Hello"))
# reverse("ello") + 'H'
# reverse("llo") + 'e'+ 'H'
# reverse("lo") + 'l'+ 'e'+ 'H'
# reverse("o")+ 'l' +'l'+ 'e'+ 'H'
# olleH
