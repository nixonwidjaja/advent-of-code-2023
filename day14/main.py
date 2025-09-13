def solve(graph):
    n, m = len(graph), len(graph[0])
    ans = 0
    for j in range(m):
        base = 0
        for i in range(n):
            if graph[i][j] == "O":
                ans += n - base
                base += 1
            elif graph[i][j] == "#":
                base = i + 1
    return ans


def spin(graph):
    n, m = len(graph), len(graph[0])
    new_graph = [["." for _ in range(m)] for _ in range(n)]
    for j in range(m):
        base = 0
        for i in range(n):
            if graph[i][j] == "O":
                new_graph[base][j] = "O"
                base += 1
            elif graph[i][j] == "#":
                new_graph[i][j] = "#"
                base = i + 1
    graph = new_graph
    new_graph = [["." for _ in range(m)] for _ in range(n)]
    for i in range(n):
        base = 0
        for j in range(m):
            if graph[i][j] == "O":
                new_graph[i][base] = "O"
                base += 1
            elif graph[i][j] == "#":
                new_graph[i][j] = "#"
                base = j + 1
    graph = new_graph
    new_graph = [["." for _ in range(m)] for _ in range(n)]
    for j in range(m):
        base = n - 1
        for i in reversed(range(n)):
            if graph[i][j] == "O":
                new_graph[base][j] = "O"
                base -= 1
            elif graph[i][j] == "#":
                new_graph[i][j] = "#"
                base = i - 1
    graph = new_graph
    new_graph = [["." for _ in range(m)] for _ in range(n)]
    for i in range(n):
        base = m - 1
        for j in reversed(range(m)):
            if graph[i][j] == "O":
                new_graph[i][base] = "O"
                base -= 1
            elif graph[i][j] == "#":
                new_graph[i][j] = "#"
                base = j - 1
    return new_graph


def solve2(graph):
    n, m = len(graph), len(graph[0])
    for k in range(200):
        graph = spin(graph)
        ans = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == "O":
                    ans += n - i
        print(k + 1, ans)


def main():
    with open("input", "r") as f:
        graph = []
        for l in f.readlines():
            graph.append(l.removesuffix("\n"))
        solve2(graph)


main()
