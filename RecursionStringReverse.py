def reverse(s):
    if (len(s) <= 1):
        return s
    else:
        m = int(len(s) / 2)
        return reverse(s[m:]) + reverse(s[:m])


print(reverse("Hello"))
# reverse(lo)+reverse(Hel)
# reverse(o)+reverse(l)+reverse(l)+reverse(He)
# reverse(e)+reverse(H)
# olleH
