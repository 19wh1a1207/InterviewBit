class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low, high = 1, A
        if A == 0:
            return 0
        while(low <= high):
            mid = (low + high)//2
            if mid * mid == A:
                return mid
            elif mid * mid > A:
                high = mid - 1
            else:
                low = mid + 1
        return high
