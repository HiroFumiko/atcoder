x = int(input())

for i in range(1, 100000):
    if i == 1:
        ans = 1
    ans *= i

    if ans == x:
        break

print(i)
