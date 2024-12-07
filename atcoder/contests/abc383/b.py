def calc_manhattan_distance(a: int, b: int, c: int, d: int) -> int:
    return abs(a - b) + abs(c - d)

def calc_threshold_list(h, w, thres_dist):
    watch_list = []
    for i in range(thres_dist):
        watch_list.append((h, w))
        watch_list.append((h-1, w))
        watch_list.append((h, w-1))
        watch_list.append((h+1, w))
        watch_list.append((h, w+1))

        watch_list.append((h, w+1))
        watch_list.append((h, w+1))

h, w, d = map(int, input().split())
s = [list(map(str, input().split())) for _ in range(w)]

count = 0
for i in range(h):
    for j in range(w):
        if s[h][w] == '.':
            for
