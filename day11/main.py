from collections import defaultdict


def solve(graph):
    n, m = len(graph), len(graph[0])
    rows, cols = defaultdict(list), defaultdict(list)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "#":
                rows[i].append(j)
    empty = 0
    new_rows = {}
    for i in range(n):
        if i not in rows:
            empty += 1000000 - 1
        else:
            new_rows[i + empty] = rows[i]
    for r in new_rows:
        for c in new_rows[r]:
            cols[c].append(r)
    new_cols = {}
    empty = 0
    for j in range(m):
        if j not in cols:
            empty += 1000000 - 1
        else:
            new_cols[j + empty] = cols[j]
    points = []
    for c in new_cols:
        for r in new_cols[c]:
            points.append((r, c))
    sum = 0
    for i in points:
        for j in points:
            sum += abs(i[0] - j[0]) + abs(i[1] - j[1])
    return sum // 2


def main():
    graph = []
    with open("input", "r") as f:
        for l in f.readlines():
            graph.append(l.removesuffix("\n"))
    print(solve(graph))


main()
