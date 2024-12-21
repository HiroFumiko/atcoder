n, a, b = input().split()
n = int(n)
s = input()
ans = []
for i in range(n):
    if s[i] != a:
        ans.append(b)
    else:
        ans.append(s[i])

print(''.join(ans))
