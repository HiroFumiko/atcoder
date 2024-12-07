n = int(input())
past_time = 0
now_time = 0
ans = 0
for i in range(n):
    now_time, v = map(int, input().split())
    if past_time != 0:
        ans -= (now_time - past_time) * 1
        if ans < 0:
            ans = 0
    ans += v
    past_time = now_time

print(ans)
