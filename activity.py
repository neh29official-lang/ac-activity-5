import math

def find_lcm(a, b):
    # LCM of two numbers can be found using the formula: (a * b) / GCD(a, b)
    # Python's math library provides a built-in gcd function (Python 3.9+)
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm_result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}") 