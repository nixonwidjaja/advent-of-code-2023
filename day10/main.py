from collections import deque

path = {
    "F": [(0, 1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "L": [(-1, 0), (0, 1)],
    "7": [(0, -1), (1, 0)],
    "-": [(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)],
}
chx = [0, 0, 1, -1]
chy = [1, -1, 0, 0]


def check_start(graph, start_x, start_y):
    paths = []
    for i in range(4):
        x, y = start_x + chx[i], start_y + chy[i]
        if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] != ".":
            for step_x, step_y in path[graph[x][y]]:
                if start_x == x + step_x and start_y == y + step_y:
                    paths.append((x, y, 1))
    return paths


def find_start(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == "S":
                return (i, j)


def solve(graph):
    n, m = len(graph), len(graph[0])
    q = deque([])
    start_x, start_y = find_start(graph)
    paths = check_start(graph, start_x, start_y)
    q.extend(paths)
    visited = {(start_x, start_y): 0}
    for x, y, _ in paths:
        visited[(x, y)] = 1
    ans = 0
    while q:
        x, y, step = q.popleft()
        ans = max(ans, step)
        for step_x, step_y in path[graph[x][y]]:
            new_x, new_y = x + step_x, y + step_y
            if (
                0 <= new_x < n
                and 0 <= new_y < m
                and graph[new_x][new_y] != "."
                and (new_x, new_y) not in visited
            ):
                q.append((new_x, new_y, step + 1))
                visited[(new_x, new_y)] = step + 1
    return ans


border = set()


def dfs(graph, now, before):
    border.add(now)
    x, y = now
    for i in range(4):
        new_x, new_y = x + chx[i], y + chy[i]
        if (
            0 <= new_x < len(graph)
            and 0 <= new_y < len(graph[0])
            and (new_x, new_y) != before
            and (new_x, new_y) not in border
            and graph[new_x][new_y] != "."
        ):
            return dfs(graph, (new_x, new_y), now)
    border.remove(now)


visited = set()


def dfs_trim(graph, x, y):
    visited.add((x, y))
    for i in range(4):
        new_x, new_y = x + chx[i], y + chy[i]
        if (
            0 <= new_x < len(graph)
            and 0 <= new_y < len(graph[0])
            and graph[new_x][new_y] != "#"
            and (new_x, new_y) not in visited
        ):
            dfs_trim(graph, new_x, new_y)


def solve2(graph):
    n, m = len(graph), len(graph[0])
    new_n, new_m = 2 * n - 1, 2 * m - 1
    start_x, start_y = find_start(graph)
    new_graph = [["." for _ in range(new_m)] for _ in range(new_n)]
    for i in range(n):
        for j in range(m):
            new_graph[2 * i][2 * j] = graph[i][j] if graph[i][j] != "S" else "F"
    for i in range(new_n):
        for j in range(new_m):
            if 0 < j < 2 * m - 2 and (new_graph[i][j - 1], new_graph[i][j + 1]) in [
                ("F", "-"),
                ("-", "-"),
                ("-", "7"),
                ("-", "J"),
                ("L", "-"),
                ("F", "7"),
                ("F", "J"),
                ("L", "J"),
                ("L", "7"),
            ]:
                new_graph[i][j] = "-"
            elif 0 < i < 2 * n - 2 and (new_graph[i - 1][j], new_graph[i + 1][j]) in [
                ("F", "|"),
                ("|", "|"),
                ("|", "L"),
                ("|", "J"),
                ("7", "|"),
                ("F", "J"),
                ("F", "L"),
                ("7", "J"),
                ("7", "L"),
            ]:
                new_graph[i][j] = "|"
    for x, y, _ in check_start(new_graph, 2 * start_x, 2 * start_y):
        dfs(new_graph, (x, y), (2 * start_x, 2 * start_y))
        break
    border.add((2 * start_x, 2 * start_y))
    for i in range(new_n):
        for j in range(new_m):
            if (i, j) in border:
                new_graph[i][j] = "#"
    for i in range(new_n):
        if new_graph[i][0] != "#":
            dfs_trim(new_graph, i, 0)
        if new_graph[i][new_m - 1] != "#":
            dfs_trim(new_graph, i, new_m - 1)
    for j in range(new_m):
        if new_graph[0][j] != "#":
            dfs_trim(new_graph, 0, j)
        if new_graph[new_n - 1][j] != "#":
            dfs_trim(new_graph, new_n - 1, j)
    for i in range(new_n):
        for j in range(new_m):
            if (i, j) in visited:
                new_graph[i][j] = "x"
    count = 0
    for i in range(0, new_n, 2):
        for j in range(0, new_m, 2):
            if new_graph[i][j] not in ["#", "x"]:
                new_graph[i][j] = "O"
                count += 1
    return count


def main():
    import sys

    sys.setrecursionlimit(100000)
    graph = []
    with open("input", "r") as f:
        for l in f.readlines():
            graph.append(l.removesuffix("\n"))
    print(solve2(graph))


main()
