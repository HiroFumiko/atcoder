def main():
    s = input()
    a_loc = []
    b_loc = []
    c_loc = []
    for i, char in enumerate(s):
        if char == 'A':
            a_loc.append(i)
        elif char == 'B':
            b_loc.append(i)
        elif char == 'C':
            c_loc.append(i)

    count = 0
    if len(a_loc) == 0 or len(b_loc) == 0 or len(c_loc) == 0:
        print(count)
    else:
        for i in a_loc:
            for j in b_loc:
                for k in c_loc:
                    if j - i == k - j and j > i and k > j:
                        count += 1
        print(count)


if __name__ == '__main__':
    main()
