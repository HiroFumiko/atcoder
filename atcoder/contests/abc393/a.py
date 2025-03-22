def main():
    takahashi, aoki = map(str, input().split())
    if takahashi == 'fine' and aoki == 'fine':
        print(4)
    if takahashi == 'fine' and aoki == 'sick':
        print(3)
    if takahashi == 'sick' and aoki == 'fine':
        print(2)
    if takahashi == 'sick' and aoki == 'sick':
        print(1)


if __name__ == '__main__':
    main()
