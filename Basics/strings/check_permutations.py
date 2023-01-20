def perm_check(s1, s2):
    n1 = len(s1)
    n2 = len(s1)

    frequency = [0] * 256

    if n1 != n2:
        return False

    for i in range(n1 - 1):
        frequency[ord(s1[i])] += 1

    for i in range(n2 - 1):
        frequency[ord(s2[i])] -= 1

    if frequency != [0] * 256:
        return False
    else:
        return True


s1 = input()
s2 = input()

if perm_check(s1, s2):
    print("true")

else:
    print("false")




