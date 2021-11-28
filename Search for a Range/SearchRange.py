class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def searchRange(self, A, B):
        res = -1
        low, high = 0, len(A) - 1
        while(low <= high):
            mid = (low + high)//2
            if A[mid] == B:
                res = mid
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        leftMost = res
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
        rightMost = res
        return [leftMost, rightMost]
