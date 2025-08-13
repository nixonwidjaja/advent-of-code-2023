def transform(val, rules):
    for src, dst, r in rules:
        if src <= val < src + r:
            return dst + val - src
    return val


def transform_interval(interval, rules):
    transformed = []
    leftover = [interval]
    for src, dst, r in rules:
        next_leftover = []
        for L, R in leftover:
            l = max(L, src)
            r = min(R, src + r - 1)
            if l > r:
                next_leftover.append((L, R))
                continue
            transformed.append((dst + l - src, dst + r - src))
            if l > L:
                next_leftover.append((L, l - 1))
            if r < R:
                next_leftover.append((r + 1, R))
        leftover = next_leftover
    return transformed + leftover


def main():
    with open("input", "r") as f:
        ls = f.readlines()
        seeds = []
        rules = []
        for l in ls:
            words = l.removesuffix("\n").split(" ")
            if words[0] == "seeds:":
                words = list(map(int, words[1:]))
                for i in range(0, len(words), 2):
                    seeds.append((words[i], words[i] + words[i + 1] - 1))
                continue
            if len(words) == 3:
                words = list(map(int, words))
                rules.append((words[1], words[0], words[2]))
                continue
            if len(words) == 1:
                next_seeds = []
                for interval in seeds:
                    next_seeds.extend(transform_interval(interval, rules))
                seeds = next_seeds
                rules = []
        next_seeds = []
        for interval in seeds:
            next_seeds.extend(transform_interval(interval, rules))
        seeds = next_seeds
        print(min(seeds))


main()
