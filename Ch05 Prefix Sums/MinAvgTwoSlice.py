"""

problem link : https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

result link : https://app.codility.com/demo/results/training6WAQ5A-R8M/

"""


def solution(A):
    # write your code in Python 3.6
    min_avg = (A[0] + A[1]) / 2
    min_idx = 0
    L = len(A)
    for i in range(2, L):
        avg = (A[i - 2] + A[i - 1] + A[i]) / 3
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 2

        avg = (A[i] + A[i - 1]) / 2
        if avg < min_avg:
            min_avg = avg
            min_idx = i - 1

    return min_idx