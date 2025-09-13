from collections import defaultdict


def hash(s):
    h = 0
    for i in s:
        h += ord(i)
        h *= 17
        h %= 256
    return h


def solve(l):
    d = defaultdict(list)
    for s in l:
        if s[-1] == "-":
            key = s[:-1]
            for i in d[hash(key)]:
                if i[0] == key:
                    d[hash(key)].remove(i)
                    break
        else:
            key, val = s.split("=")
            val = int(val)
            exist = False
            for i, v in enumerate(d[hash(key)]):
                if v[0] == key:
                    exist = True
                    d[hash(key)][i] = (key, val)
                    break
            if not exist:
                d[hash(key)].append((key, val))
    ans = 0
    for b, v in d.items():
        for i, val in enumerate(v):
            ans += (b + 1) * (i + 1) * val[1]
    return ans


def main():
    with open("input", "r") as f:
        l = f.readline().split(",")
        print(solve(l))


main()
