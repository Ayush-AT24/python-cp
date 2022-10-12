from math import gcd, lcm
t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    for i in range(n-1):
        b.append(lcm(a[i], a[i+1]))
    b.append(a[-1])
    flag = False
    for i in range(n):
        if gcd(b[i], b[i+1]) != a[i]:
            print("NO")
            flag = True
            break
    if not flag:
        print("YES")

    t-=1

