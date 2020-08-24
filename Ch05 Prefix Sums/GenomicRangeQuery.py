"""

problem link: https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

"""

"""
1. 시간 복잡도 초과 풀이

result link : https://app.codility.com/demo/results/trainingYM45DA-DRB/

"""

from collections import Counter


def solution1(S, P, Q):
    # write your code in Python 3.6

    c = Counter()
    acc = []
    for char in S:
        c += Counter(char)
        acc.append(c.copy())

    ans = []
    for p, q in zip(P, Q):

        sub = acc[q] - acc[p] + Counter(S[p])
        if "A" in sub:
            ans.append(1)
        elif "C" in sub:
            ans.append(2)
        elif "G" in sub:
            ans.append(3)
        elif "T" in sub:
            ans.append(4)

    return ans


"""

2. 시간 복잡도 통과 쿼리

result link : https://app.codility.com/demo/results/training3D2A9X-S3D/

"""


def solution2(S, P, Q):
    # write your code in Python 3.6
    impact_factors = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }

    counts = [0, 0, 0, 0]
    acc = []
    for char in S:
        counts[impact_factors[char] - 1] += 1
        acc.append(counts[:])

    ans = []

    for p, q in zip(P, Q):

        chars = [0, 0, 0, 0]
        i = 0
        for c1, c2 in zip(acc[p], acc[q]):
            chars[i] = c2 - c1
            i += 1
        chars[impact_factors[S[p]] - 1] += 1

        if chars[0] > 0:
            ans.append(1)
        elif chars[1] > 0:
            ans.append(2)
        elif chars[2] > 0:
            ans.append(3)
        elif chars[3] > 0:
            ans.append(4)

    return ans
