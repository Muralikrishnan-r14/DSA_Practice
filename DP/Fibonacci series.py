
'''def f(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]
    dp[n] = f(n - 1, dp) + f(n - 2, dp)
    return dp[n]


if __name__ == "__main__":
    n = 5
    dp = [-1] * (n + 1)
    print(f(n, dp))'''
from typing import List
'''def main():
    n = 5
    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])
if __name__ == "__main__":
    main()'''
def main():
    n = 5

    prev2 = 0
    prev = 1

    for i in range(2, n+1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i
    print(prev)

if __name__ == "__main__":
    main()