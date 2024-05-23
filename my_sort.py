# 1. import heaqp

import heapq

nums = [1, 2, 5, 7, 9, 19, 2, 4, 91, 4]
n = 3
max_n = heapq.nlargest(n, nums)
min_n = heapq.nsmallest(n, nums)
# print(max_n)
# print(min_n)


portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares": 50, "price": 543.22},
    {"name": "FB", "shares": 200, "price": 21.09},
    {"name": "HPQ", "shares": 35, "price": 31.75},
    {"name": "YHOO", "shares": 45, "price": 16.35},
    {"name": "ACME", "shares": 75, "price": 115.65},
]

# portfolio is a iterable, and s is one of the elements of iterable portfolio

portfolio_max_n = heapq.nlargest(1, portfolio, key=lambda s: s["price"])

# print(portfolio_max_n)

# 2. function : sorted() and slice n

# print(sorted(nums)[:3])
# print(sorted(nums)[-3:])

# print(sorted(portfolio, key=lambda s: s["price"], reverse=True)[:1])
# print(sorted(portfolio, key=lambda s: s["price"])[:1])

from collections import defaultdict

# d = defaultdict(list)
# d["a"].append(1)
# d["b"].append(2)
# d["b"].append(2)
# d["c"].append(3)

# print(d)

d = defaultdict(set)
d["a"].add(1)
d["a"].add(2)
d["a"].add(3)

d["b"].add(1)
d["c"].add(2)
d["c"].add(3)

print(d)
