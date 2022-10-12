s = input()
if s[0] != '-':
    print(s)
else:
    if s[-1] > s[-2]:
        s = s[:-1]
    else:
        s = s[:-2] + s[-1]
    if len(s) == 2 and s[1] == '0':
        s = s[1]
    print(s)

