class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        MAX, MIN = A[0], A[0]
        for i in range(1, len(A)):
            if A[i] > MAX:
                MAX = A[i]
            if A[i] < MIN:
                MIN = A[i]
        return MAX + MIN
