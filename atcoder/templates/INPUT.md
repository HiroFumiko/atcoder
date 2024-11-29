```python
#str型で受け取るとき
s = input()

#int型で受け取るとき
s = int(input())

#float型　(小数)で受け取るとき
s = float(input())

#list型で受け取るとき
s = input().split()

#出力
print(s)  # ['Alice', 'Bob', 'Charlie']
print(s[0])  # Alice
print(s[0][0])  # A

#複数の整数で受け取るとき
A, B = map(int, input().split())

#出力
print(A)  # 1
print(A, B)  # 1 3

#list型で取得
l = list(map(int, input().split()))

#出力
print(l)  # [1, 3, 4, 5, 6]

#文字と数字の複合型で受け取るとき
N, S = map(str, input().split())
```
