def match_grid(array, target):
    for i in range(len(array)):
        if array[i] != target[i]:
            return False
    return True


def main():
    n, m = map(int, input().split())
    grid_s = []
    grid_t = []
    for _ in range(n):
        grid_s.append(list(input()))

    for _ in range(m):
        grid_t.append(list(input()))

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            array = []
            for k in range(m):
                array.append(grid_s[i + k][j:j + m])

            if match_grid(array, grid_t):
                print(i+1, j+1)
                return


if __name__ == "__main__":
    main()
