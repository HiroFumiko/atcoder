import itertools
import pandas as pd

a, b, c, d, e = map(int, input().split())

persons: list[str] = []
for i in range(5):
    for comb in itertools.combinations(['A', 'B', 'C', 'D', 'E'], i+1):
        persons.append(''.join(comb))

persons.reverse() # 参加者の順番を逆順にする

scores = []
for name in persons:
    name_score = 0
    if "A" in name:
        name_score += a
    if "B" in name:
        name_score += b
    if "C" in name:
        name_score += c
    if "D" in name:
        name_score += d
    if "E" in name:
        name_score += e
    scores.append(name_score)

df_name = pd.DataFrame({
    "Name": persons,
    "Score": scores
})
df_name.sort_values(by=["Score", "Name"], ascending=[False, True], inplace=True)

ans_list = df_name["Name"].tolist()
for ans in ans_list:
    print(ans)
