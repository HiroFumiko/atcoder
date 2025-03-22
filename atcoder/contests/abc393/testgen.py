import random

def generate_testcase(filename="testcase_multiple_edges.txt"):
    """ 20個の多重辺を含むグラフを生成してファイルに出力 """
    N = 50  # 頂点数
    M = 70  # 辺数（うち20本は多重辺）

    edges = set()

    # まず50本の異なる辺を作成（M - 多重辺の数）
    while len(edges) < 50:
        u = random.randint(1, N)
        v = random.randint(1, N)
        if u != v:
            edges.add((min(u, v), max(u, v)))  # 無向グラフなので順序統一

    unique_edges = list(edges)

    # 既存の辺から20本を選び、多重辺を作成
    multiple_edges = random.choices(unique_edges, k=20)  # sample → choices に変更（重複あり）

    with open(filename, "w") as f:
        f.write(f"{N} {M}\n")
        for u, v in unique_edges:
            f.write(f"{u} {v}\n")
        for u, v in multiple_edges:
            f.write(f"{u} {v}\n")  # 同じ辺を再び追加（多重辺）

# テストケースを作成
generate_testcase()

print("正しく70本の辺を持つテストケースを生成しました。")
