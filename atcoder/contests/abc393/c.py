def main():
    _, m = map(int, input().split())
    edges = set()
    count = 0
    for i in range(m):
        u_i, v_i = map(int, input().split())
        edge = tuple(sorted((u_i, v_i)))

        if u_i == v_i:
            count += 1

        if edge in edges:
            count += 1
        edges.add(edge)

    print(count)


if __name__ == '__main__':
    main()
