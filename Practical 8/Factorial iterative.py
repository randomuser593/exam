def get_factorial_while_loop(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

inp = input("Enter a number: ")
inp = int(inp)

print(f"The result is: {get_factorial_while_loop(inp)}")