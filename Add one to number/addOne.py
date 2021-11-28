class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = ""
        for i in A:
            s += str(i)
        s2 = str(int(s) + 1)
        a = []
        for i in s2:
            a.append(int(i))
        return a
