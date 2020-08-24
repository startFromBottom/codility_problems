"""

problem link : https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/


result : https://app.codility.com/demo/results/trainingP27Q6Z-CS8/

"""

from collections import Counter


def solution(N, A):
    # write your code in Python 3.6

    L = len(A)
    c = Counter()
    common = 0

    for i in range(L):
        if A[i] == N + 1:
            most_common = c.most_common(1)
            if most_common:
                common += most_common[0][1]  # most count
            c = Counter()  # reset
        else:
            c[A[i]] += 1

    ans = [common] * N
    for k, v in c.items():
        ans[k - 1] += v

    return ans
