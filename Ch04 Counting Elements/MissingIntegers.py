"""

problem link : https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

result : https://app.codility.com/demo/results/trainingETTG9E-G32/

"""


def solution(A):
    A = sorted(list(set(A)))

    # ex) A = [98, 99, 100] -> 1
    if A[0] > 1:
        return 1

    for i in range(1, len(A)):
        # ex) A = [1,2,4,5] -> 3
        if A[i - 1] >= 0 and A[i] > A[i - 1] + 1:
            return A[i - 1] + 1
        # ex) A = [-3,-1, 3] -> 1
        elif A[i - 1] <= 0 and A[i] > 1:
            return 1

    # ex) A = [-3, -1] -> 1
    if A[-1] <= 0:
        return 1
    # ex) A = [1, 2, 3] -> 4
    return A[-1] + 1
