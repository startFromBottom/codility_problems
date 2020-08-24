"""

problem link : https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

result : https://app.codility.com/demo/results/trainingFH9KJE-8XM/

"""


def solution(A, B, K):
    # write your code in Python 3.6

    ans = (B // K - A // K)
    if A % K == 0:
        ans += 1
    return ans
