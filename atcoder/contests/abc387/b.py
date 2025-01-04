kuku_grid: list[list[int]] = []
for i in range(1, 10):
    kuku = []
    for j in range(1, 10):
        kuku.append(i*j)
    kuku_grid.append(kuku)

n = int(input())

ans = 0
for i in range(9):
    for j in range(9):
        ans += kuku_grid[i][j]

for i in range(9):
    if n in kuku_grid[i]:
        ans -= n

print(ans)
