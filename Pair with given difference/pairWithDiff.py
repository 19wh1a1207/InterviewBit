class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        p1, p2 = 0, 1
        while(p1 < len(A) and p2 < len(A)):
            if (p1 != p2) and (A[p2] - A[p1]) == B:
                return 1
            elif (A[p2] - A[p1]) > B:
                p1 += 1
            else:
                p2 += 1
        return 0
