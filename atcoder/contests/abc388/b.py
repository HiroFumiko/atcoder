n, d = map(int, input().split())
t = []
l = []
for i in range(n):
    t_tmp, l_tmp = map(int, input().split())
    t.append(t_tmp)
    l.append(l_tmp)

for k in range(1, d+1):
    snake_weights = []
    for j in range(n):
        snake_weights.append(t[j] * (l[j] + k))

    print(max(snake_weights))
