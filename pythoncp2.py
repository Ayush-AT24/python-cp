t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        if i - a[i-1]-1 >= 0 and dp[i - a[i-1]-1]:
            dp[i] = True
        if i + a[i-1] <= n and dp[i-1]:
            dp[i+a[i-1]] = True
    print("YES" if dp[n] else "NO")
    t-=1
