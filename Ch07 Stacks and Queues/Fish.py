"""

problem link : https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

"""


def solution(A, B):
    # write your code in Python 3.6

    L = len(A)
    stack = []
    for i in range(L):
        if B[i] == 0:
            if not stack or stack[-1] > 0:
                stack.append(A[i])
            elif stack and A[i] > abs(stack[-1]):
                while stack and stack[-1] < 0 and A[i] > abs(stack[-1]):
                    stack.pop()
                if not stack or stack[-1] > 0:
                    stack.append(A[i])

        else:
            stack.append(-A[i])

    return len(stack)
