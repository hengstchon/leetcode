# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2,n):
            if i * i >= n:
                break
            if isPrime[i] == False:
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False
        return sum(isPrime)
