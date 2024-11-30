n, m = map(int, input().split())
people = list(map(int, input().split()))
sushi = list(map(int, input().split()))

for i in sushi:
    for j in range(len(people)):
        if i < min(people):
            print(-1)
            break

        if i >= people[j]:
            print(j+1)
            break
