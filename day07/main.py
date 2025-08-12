from collections import Counter

card_rank = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.ranks = [card_rank[i] for i in cards]
        self.bid = bid
        counter = Counter(cards)
        max_card = max(counter.items(), key=lambda x: x[1])
        if max_card[0] == "J":
            val = counter.pop("J")
            if val == 5:
                self.strength = 10
                return
            counter[max(counter.items(), key=lambda x: x[1])[0]] += val
        elif "J" in counter:
            val = counter.pop("J")
            counter[max_card[0]] += val
        sorted_count = sorted(list(counter.items()), key=lambda x: x[1], reverse=True)
        ss = "".join([str(i[1]) for i in sorted_count])
        self.strength = 0
        if ss == "5":
            self.strength = 10
        elif ss == "41":
            self.strength = 9
        elif ss == "32":
            self.strength = 8
        elif ss == "311":
            self.strength = 7
        elif ss == "221":
            self.strength = 6
        elif ss == "2111":
            self.strength = 5

    def __lt__(self, other):
        if self.strength == other.strength:
            return self.ranks < other.ranks
        return self.strength < other.strength

    def __repr__(self):
        return f"{self.cards} {self.strength}"


def main():
    with open("input", "r") as f:
        ls = f.readlines()
        cards = []
        for l in ls:
            card, b = l.split(" ")
            cards.append(Hand(card, int(b)))
        cards.sort()
    ans = 0
    for i, c in enumerate(cards):
        ans += (i + 1) * c.bid
    print(ans)


main()
