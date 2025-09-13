from collections import defaultdict


def solve(graph):
    n, m = len(graph), len(graph[0])
    rows = defaultdict(list)
    for i in range(n):
        rows[graph[i]].append(i)
    ans = check(n, set(map(tuple, rows.values())), graph, -1) * 100
    cols = defaultdict(list)
    inv_graph = []
    for j in range(m):
        c = []
        for i in range(n):
            c.append(graph[i][j])
        col = "".join(c)
        cols[col].append(j)
        inv_graph.append(col)
    return ans + check(m, set(map(tuple, cols.values())), inv_graph, -1)


def solve2(graph):
    n, m = len(graph), len(graph[0])
    rows = defaultdict(list)
    for i in range(n):
        rows[graph[i]].append(i)
    old_result = check(n, set(map(tuple, rows.values())), graph, -1)
    for k, row in generate_changes(rows):
        old_row = graph[k]
        graph[k] = row
        new_rows = defaultdict(list)
        for i in range(n):
            new_rows[graph[i]].append(i)
        new_result = check(n, set(map(tuple, new_rows.values())), graph, old_result)
        if new_result > 0 and new_result != old_result:
            return new_result * 100
        graph[k] = old_row

    cols = defaultdict(list)
    inv_graph = []
    for j in range(m):
        c = []
        for i in range(n):
            c.append(graph[i][j])
        col = "".join(c)
        cols[col].append(j)
        inv_graph.append(col)
    old_result = check(m, set(map(tuple, cols.values())), inv_graph, -1)
    for k, col in generate_changes(cols):
        old_col = inv_graph[k]
        inv_graph[k] = col
        new_cols = defaultdict(list)
        for i in range(m):
            new_cols[inv_graph[i]].append(i)
        new_result = check(m, set(map(tuple, new_cols.values())), inv_graph, old_result)
        if new_result > 0 and new_result != old_result:
            return new_result
        inv_graph[k] = old_col
    return check(m, set(map(tuple, cols.values())), inv_graph)


def check(n, indices, graph, old_result):
    adj = []
    for i in indices:
        if len(i) >= 2:
            for k in range(len(i) - 1):
                if i[k] + 1 == i[k + 1]:
                    adj.append((i[k], i[k + 1]))
    if len(adj) == 0:
        return 0
    for a, b in adj:
        L, R = a, b
        valid = True
        while L >= 0 and R < n:
            if graph[L] != graph[R]:
                valid = False
                break
            L -= 1
            R += 1
        if valid and a + 1 != old_result:
            return a + 1
    return 0


def can_transform(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count == 1


def generate_changes(rows):
    changes = []
    for k1, v1 in rows.items():
        for k2, v2 in rows.items():
            if not can_transform(k1, k2):
                continue
            for i in v1:
                changes.append((i, k2))
            for i in v2:
                changes.append((i, k1))
    return changes


def main():
    with open("input", "r") as f:
        ans = 0
        graph = []
        for l in f.readlines():
            l = l.removesuffix("\n")
            if len(l) == 0:
                ans += solve2(graph)
                graph = []
                continue
            graph.append(l)
        ans += solve2(graph)
        print(ans)


main()
