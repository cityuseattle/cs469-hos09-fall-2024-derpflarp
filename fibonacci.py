# def fib_rec(n):
#     if n < 2:
#         return n
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)
    
# print(fib_rec(6))

# print(fib_rec(100))

def fib_dp1(n):
    memo = [None] * (n+1)
    
    def fib(n):
        if n < 2:
            memo[n] = n
        if memo[n] is None:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

    return fib(n)

print(fib_dp1(6))

print(fib_dp1(100))

def fib_dp2(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(fib_dp2(6))

print(fib_dp2(100))