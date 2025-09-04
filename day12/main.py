def solve(s, nums):
    memo = {}

    def f(s, nums):
        if len(nums) == 0:
            return 1 if "#" not in s else 0
        if len(s) == 0:
            return 0
        if (s, nums) in memo:
            return memo[(s, nums)]
        count = 0
        if s[0] in ".?":
            count += f(s[1:], nums)
        if s[0] in "#?" and len(s) >= nums[0] and "." not in s[: nums[0]]:
            if len(s) == nums[0]:
                count += f("", nums[1:])
            elif len(s) > nums[0] and s[nums[0]] != "#":
                count += f(s[nums[0] + 1 :], nums[1:])
        memo[(s, nums)] = count
        return count

    return f(s, nums)


def main():
    with open("input", "r") as f:
        ans = 0
        from time import time

        start = time()
        for l in f.readlines():
            s = l.removesuffix("\n").split(" ")
            nums = tuple(map(int, s[1].split(",")))
            ans += solve((s[0] + "?") * 4 + s[0], nums * 5)
        print(ans)
        print(time() - start)


main()
