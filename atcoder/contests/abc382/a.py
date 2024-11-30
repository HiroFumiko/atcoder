n, d = map(int, input().split())
s = input()

empty = 0
for b in s:
    if b == ".":
        empty += 1

print(empty + d)
