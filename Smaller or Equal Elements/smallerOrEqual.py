class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res = -1
        low, high = 0, len(A) - 1
        while(low <= high):
            mid = (low + high)//2
            if A[mid] == B:
                res = mid
                low = mid + 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        if res == -1:
            return high + 1
        return res + 1
