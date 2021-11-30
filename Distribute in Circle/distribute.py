class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if C % B == 0:
            C = B
        else:
            C = C % B
        if A % B == 0:
            A = B
        else:
            A = A % B
        return (A + C - 1) % B
