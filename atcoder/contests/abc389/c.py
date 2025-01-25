q = int(input())

array: list[int] = []
heads: list[int] = []
for _ in range(q):
    qu = input()
    if qu[0] == '1':
        t, length = map(int, qu.split())
        if len(array) == 0:
            heads.append(0)
        else:
            h = heads[-1] + array[-1]
            heads.append(h)
        array.append(length)
    elif qu[0] == '2':
        m = array.pop(0)
        heads.pop(0)
        heads = [h - m for h in heads]
    elif qu[0] == '3':
        t, length = map(int, qu.split())
        print(heads[length-1])
