def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    n = int(input("Enter N: "))
    print("Fibonacci:", fibonacci(n))
    print("Factorial:", factorial(n))


if __name__ == '__main__':
    main()