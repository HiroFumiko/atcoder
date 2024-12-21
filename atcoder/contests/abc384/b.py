def is_appropriate_rate(rate: int, division: int) -> bool:
    if rate >= 1600 and rate <= 2799 and division == 1:
        return True
    elif rate >= 1200 and rate <= 2399 and division == 2:
        return True
    else:
        return False


def main():
    n, r = map(int, input().split())
    for _ in range(n):
        d, a = map(int, input().split())
        if is_appropriate_rate(r, d):
            r += a

    print(r)


if __name__ == '__main__':
    main()
