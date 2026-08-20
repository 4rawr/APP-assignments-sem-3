def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    seq = fibonacci(n - 1, memo)
    next_val = seq[-1] + seq[-2]
    seq.append(next_val)
    return seq

n = int(input("Enter N: "))
print(fibonacci(n))
