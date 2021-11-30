class Solution:
    # @param A : integer
    # @return a list of integers
    def isPrime(self, n):
        f = 0
        if n == 1:
            return -1
        for i in range(1, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                f += 1
        return f

    def primesum(self, A):
        for i in range(2, A):
            if self.isPrime(i) == 1 and self.isPrime(A - i) == 1:
                return [int(i), int(A - i)]
