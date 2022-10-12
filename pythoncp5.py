s = input()
s = s[1:-1]
s = s.split(', ')
if s[-1] == '':
    s.clear()
s = set(s)
print(len(s))
