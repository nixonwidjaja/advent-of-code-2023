chx = [0, 0, 1, -1]
chy = [1, -1, 0, 0]


def solve(graph, initial_state):
    n, m = len(graph), len(graph[0])
    q = [initial_state]
    visited = set()
    path = set()
    while q:
        x, y, dir = q.pop()
        if x < 0 or x >= n or y < 0 or y >= m or (x, y, dir) in visited:
            continue
        path.add((x, y))
        visited.add((x, y, dir))
        if graph[x][y] == "|":
            q.extend(
                [
                    [(x - 1, y, 3), (x + 1, y, 2)],
                    [(x - 1, y, 3), (x + 1, y, 2)],
                    [(x + chx[dir], y + chy[dir], dir)],
                    [(x + chx[dir], y + chy[dir], dir)],
                ][dir]
            )
        elif graph[x][y] == "-":
            q.extend(
                [
                    [(x + chx[dir], y + chy[dir], dir)],
                    [(x + chx[dir], y + chy[dir], dir)],
                    [(x, y - 1, 1), (x, y + 1, 0)],
                    [(x, y - 1, 1), (x, y + 1, 0)],
                ][dir]
            )
        elif graph[x][y] == "/":
            q.append([(x - 1, y, 3), (x + 1, y, 2), (x, y - 1, 1), (x, y + 1, 0)][dir])
        elif graph[x][y] == "\\":
            q.append([(x + 1, y, 2), (x - 1, y, 3), (x, y + 1, 0), (x, y - 1, 1)][dir])
        else:
            q.append((x + chx[dir], y + chy[dir], dir))
    return len(path)


def solve2(graph):
    n, m = len(graph), len(graph[0])
    states = []
    for i in range(n):
        states.append((i, 0, 0))
        states.append((i, m - 1, 1))
    for j in range(m):
        states.append((0, j, 2))
        states.append((n - 1, j, 3))
    ans = 0
    for initial_state in states:
        ans = max(ans, solve(graph, initial_state))
    return ans


def main():
    with open("input", "r") as f:
        graph = []
        for l in f.readlines():
            graph.append(l.removesuffix("\n"))
        print(solve2(graph))


main()
