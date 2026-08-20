def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    dp = [0, 1]
    for _ in range(2, n):
        dp.append(dp[-1] + dp[-2])
    return dp

n = int(input("Enter N: "))
print(fibonacci(n))
