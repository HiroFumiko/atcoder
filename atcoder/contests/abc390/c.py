def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(list(map(str, input().split())))
    print(s)


if __name__ == "__main__":
    main()
