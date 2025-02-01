def check(array):
    ratio = array[1] / array[0]
    for i in range(len(array) - 1):
        current_ratio = array[i+1] / array[i]
        if abs(current_ratio - ratio) > 1e-9:
            return False
    return True


def main():
    _ = int(input())
    array = list(map(int, input().split()))
    if check(array):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
