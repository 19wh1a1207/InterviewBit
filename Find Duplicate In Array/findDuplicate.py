class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count = [0] * (max(A) + 1)
        for i in range(len(A)):
            count[A[i]] += 1
            if count[A[i]] == 2:
                return A[i]
        return -1 
