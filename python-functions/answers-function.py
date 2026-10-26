# 1. Write a function `greet()` that prints `"Welcome to Python Programming"`.
def greet():
    print("Welcome to Python Programming.")
greet()

# 2. Write a function `add(a, b)` that accepts two numbers and returns their sum.
def add(a,b):
    return a + b
print(add(5,4))

# 3. Write a function `square(n)` that returns the square of a given number.
def square(n):
    return n**2
print(square(5))

# 4. Write a function `check_even(n)` that checks whether a number is even or odd.
def check_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even(6))
print(check_even(9))


# 5. Write a function `largest(a, b, c)` that returns the largest among three numbers without using `max()`.
def largest_number(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(largest_number(7,7,8))

# 6. Write a function `factorial(n)` that calculates the factorial of a number using a loop.
def factorial(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(n,0,-1):
            fact *= i
        return fact
print(factorial(5))

# 7. Write a function `reverse_string(s)` that reverses a string without using `[::-1]`.
def reverse_string(s):
    rev = ""
    for i in s:
        rev = i+rev
    return rev
print(reverse_string("Python"))

# 8. Write a function `count_vowels(s)` that counts the vowels in a given string.
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "AEIOUaeiou":
            count+=1
    return count
print(count_vowels("Aadi is the best."))

# 9. Write a function `is_prime(n)` that checks whether a number is prime.
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return "Not Prime"
        else:
            return "Prime"
print(is_prime(5))

# 10. Write a function `sum_digits(n)` that calculates the sum of the digits of an integer.
def sum_digits(n):
    digit_sum = 0
    for i in str(n):
        digit_sum += int(i)

    return digit_sum
print(sum_digits(56))
