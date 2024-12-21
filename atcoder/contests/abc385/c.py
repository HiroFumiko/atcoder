def check_num(h: list[int], i: int, dist: int):
    if len(h) <= dist:
        return True
    elif h[i] != h[i + dist]:
        return False
    elif h[i] == h[i + dist] and i + dist <= len(h) - 1:
        return check_num(h, i + dist, dist)


def main():
    n = int(input())
    h = list(map(int, input().split()))

    if len(h) == len(set(h)):
        print(1)
    else:
        for i in range(n):
