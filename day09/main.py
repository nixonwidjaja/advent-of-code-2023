def solve(arr):
    diff = [arr]
    is_diff = True
    while is_diff:
        next_diff = []
        for i in range(len(diff[-1]) - 1):
            next_diff.append(diff[-1][i + 1] - diff[-1][i])
        is_diff = check_diff(next_diff)
        diff.append(next_diff)
    before = 0
    for i in reversed(diff):
        before = i[0] - before
    return before


def check_diff(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return True
    return False


def main():
    with open("input", "r") as f:
        ans = 0
        for l in f.readlines():
            arr = l.removesuffix("\n").split(" ")
            ans += solve(list(map(int, arr)))
        print(ans)


main()
