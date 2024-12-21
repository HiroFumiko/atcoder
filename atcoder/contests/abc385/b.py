class Fields:
    def __init__(self, x: int, y: int, s: list[list[str]]):
        self.ticker: str = s[y][x]
        self.is_visited: bool = False


def main():
    h, w, x, y = map(int, input().split())
    s = []
    for i in range(h):
        s.append([j for j in input()])
    t = input()

    maps = []
    for i in range(h):
        maps.append([Fields(j, i, s) for j in range(w)])

    # 原点基準を変更
    x -= 1
    y -= 1

    count = 0

    for move in t:
        pre_x = x
        pre_y = y

        if move == 'U':
            x -= 1
        if move == 'D':
            x += 1
        if move == 'L':
            y -= 1
        if move == 'R':
            y += 1

        if maps[x][y].ticker == '#':
            x = pre_x
            y = pre_y
        elif maps[x][y].ticker == '@' and not maps[x][y].is_visited:
            count += 1
            maps[x][y].is_visited = True

    print(x+1, y+1, count)


if __name__ == '__main__':
    main()
