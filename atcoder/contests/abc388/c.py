import bisect


def max_find_half_index(arr, k, hi):
    half_index = k / 2
    index = bisect.bisect_right(arr, x=half_index, hi=hi)
    return index


def kagamimochi(arr):
    d = [0 for _ in range(len(arr))]
    tmp = 0
    for i in range(len(arr)):
        if i == 0:
            d[i] = 0
        elif arr[i] == arr[i-1]:
            d[i] = d[i-1] + tmp
        elif arr[i] > arr[i-1]:
            max_index = max_find_half_index(arr, arr[i], i)
            d[i] = d[i-1] + max_index
            tmp = d[i]
        else:
            pass
    return d


def main():
    int(input())
    a = list(map(int, input().split()))
    d = kagamimochi(a)
    print(d[-1])


if __name__ == '__main__':
    main()
