def check(array):
    flag = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            flag = False
            break
    return flag


def work(array, idx):
    new_array = [a for a in array]
    new_array[idx], new_array[idx+1] = array[idx+1], array[idx]
    return new_array


def main():
    array = list(map(int, input().split()))
    flag = False
    for i in range(len(array) - 1):
        changed_array = work(array, i)
        if check(changed_array):
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
