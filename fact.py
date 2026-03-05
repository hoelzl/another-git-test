def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    print(fact(5))  # Output: 120    print(fact(0))  # Output: 1
    print(fact(10)) # Output: 3628800