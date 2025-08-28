def fibonacci(n):
 
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    terms = int(input("ENTER THE SIZE: "))
    print("fibonacci:")
    print(fibonacci(terms))
