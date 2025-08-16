import math


def solve(graph, steps):
    count = 0
    now = "AAA"
    while now != "ZZZ":
        now = graph[now][steps[count % len(steps)]]
        count += 1
    return count


def solve2(graph, steps):
    now = []
    count = 0
    for k in graph:
        if k[-1] == "A":
            now.append(k)
    indices = [0 for _ in range(len(now))]
    for i in range(len(now)):
        count = 0
        while now[i][-1] != "Z":
            now[i] = graph[now[i]][steps[count % len(steps)]]
            count += 1
            if now[i][-1] == "Z":
                indices[i] = count
    return math.lcm(*indices)


def check_finish(state):
    for s in state:
        if s[-1] != "Z":
            return False
    return True


def main():
    with open("input", "r") as f:
        ls = f.readlines()
        steps = []
        for i in ls[0].removesuffix("\n"):
            steps.append(1 if i == "R" else 0)
        graph = {}
        for l in ls[2:]:
            s = l.split(" ")
            graph[s[0]] = (s[2][1:-1], s[3].removesuffix("\n")[:-1])
        print(solve2(graph, steps))


main()
