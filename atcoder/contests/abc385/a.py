a, b, c = map(int, input().split())

if a == b and b == c:
    print("Yes")
elif a + b == c or a + c == b or b + c == a:
    print("Yes")
else:
    print("No")
