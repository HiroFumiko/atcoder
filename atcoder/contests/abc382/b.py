n, d = map(int, input().split())
s = input()

boxes = [char for char in s]
for i in range(d):
    for j in range(len(boxes)-1, -1, -1):
        if boxes[j] == "@":
            boxes[j] = "."
            break

print("".join(boxes))
