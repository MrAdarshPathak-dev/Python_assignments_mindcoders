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

# 11. Write a function `calculate(a, b)` that returns the sum, difference, product, and quotient of two numbers.
def calculate(a, b):
    if b == 0:
        return a+b, a-b, a*b, "undefined"
    return a+b, a-b, a*b, a/b

total, difference, product, quotient = calculate(50, 0)

print(total)
print(difference)
print(product)

if quotient == "undefined":
    print("Cannot divide by zero")
else:
    print(quotient)


# 12. Write a function `power(base, exponent=2)` that calculates the power of a number using a default parameter.
def power(base,exponent=2):
    return base**exponent

sq = power(5)
cube = power(5,3)

print(f"Square {sq} & Cube {cube}")


# 13. Write a function `student_details(name, age, course)` and call it using keyword arguments in a different order.
def student_details(name, age, course):
    return name, age, course

name, age, course = student_details(age=20, course="BCA", name="Adarsh")

print(f"Name:{name}, Age:{age}, Course:{course}")


# 14. Write a function `simple_interest(p, r, t)` that calculates simple interest and returns the result.
def simple_interest(p,r,t):
    return (p*r*t)/100
simple_interest = simple_interest(20000,12,3)
print(simple_interest)

# 15. Write a function `find_average(*numbers)` that accepts any number of numeric arguments and returns their average.

def find_average(*numbers):
    count = 0
    total = 0
    for num in numbers:
        total+=num
        count+=1
    return total/count

average = find_average(2,4,6)

print("Average:",average)


# 16. Write a function `student_info(**kwargs)` that accepts student information such as name, age, course, and marks and prints each key-value pair.
def student_info(**informations):
    for key,value in informations.items():
        print(key, ":", value)

student_info(
    name = "Adarsh Pathak",
    course = "BCA",
    domain = "Python developer"
)


# 17. Write a function `calculate_bill(price, quantity=1, discount=0)` that returns the final bill after applying a percentage discount.
def calculate_bill(price, quantity=1, discount=0):
    net_price = (price*quantity)
    discount_amount = net_price*(discount/100)
    final_bill = net_price-discount_amount
    return final_bill

bill = calculate_bill(price=10000, quantity=5, discount=10)
print(bill)


# 18. Write a function `employee_salary(name, basic_salary, bonus=0, tax=5)` that returns the employee's name and net salary after applying the bonus and percentage tax.
def employee_salary(name, basic_salary, bonus=0, tax=5):
    tax_amount = (basic_salary+bonus)*(tax/100)
    net_salary = (basic_salary+bonus)-tax_amount
    return net_salary

in_hand_salary = employee_salary("Adarsh Pathak", 3000000, 300000, tax=30)

print("Salary in hand: ", in_hand_salary)
