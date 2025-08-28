def factorial(n):

    if n < 0:
        raise ValueError("factorial only work with positive number")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



if __name__ == "__main__":
    num = int(input("Enter the number: "))

    try:
        print(f" the factorial for  {num} is: {factorial(num)}")
    except ValueError as e:
        print(e)
