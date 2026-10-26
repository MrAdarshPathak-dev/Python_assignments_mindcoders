
# Python Functions — Assignment

**Total Questions:** 40  
**Topic:** Python Functions

**Instructions:** Solve each question independently. Test your functions with different inputs and handle edge cases wherever required.

## Part 1: Basic Functions

1. Write a function `greet()` that prints `"Welcome to Python Programming"`.

2. Write a function `add(a, b)` that accepts two numbers and returns their sum.

3. Write a function `square(n)` that returns the square of a given number.

4. Write a function `check_even(n)` that checks whether a number is even or odd.

5. Write a function `largest(a, b, c)` that returns the largest among three numbers without using `max()`.

6. Write a function `factorial(n)` that calculates the factorial of a number using a loop.

7. Write a function `reverse_string(s)` that reverses a string without using `[::-1]`.

8. Write a function `count_vowels(s)` that counts the vowels in a given string.

9. Write a function `is_prime(n)` that checks whether a number is prime.

10. Write a function `sum_digits(n)` that calculates the sum of the digits of an integer.

## Part 2: Parameters and Return Values

11. Write a function `calculate(a, b)` that returns the sum, difference, product, and quotient of two numbers.

12. Write a function `power(base, exponent=2)` that calculates the power of a number using a default parameter.

13. Write a function `student_details(name, age, course)` and call it using keyword arguments in a different order.

14. Write a function `simple_interest(p, r, t)` that calculates simple interest and returns the result.

15. Write a function `find_average(*numbers)` that accepts any number of numeric arguments and returns their average.

16. Write a function `student_info(**kwargs)` that accepts student information such as name, age, course, and marks and prints each key-value pair.

17. Write a function `calculate_bill(price, quantity=1, discount=0)` that returns the final bill after applying a percentage discount.

18. Write a function `employee_salary(name, basic_salary, bonus=0, tax=5)` that returns the employee's name and net salary after applying the bonus and percentage tax.

## Part 3: Lists, Dictionaries, and Strings

19. Write a function `remove_duplicates(lst)` that removes duplicate elements from a list without using `set()` while preserving the original order.

20. Write a function `second_largest(lst)` that returns the second-largest distinct number in a list without using `sort()` or `sorted()`.

21. Write a function `count_frequency(lst)` that returns a dictionary containing the frequency of each element.

22. Write a function `palindrome(s)` that checks whether a string is a palindrome, ignoring spaces and letter case.

23. Write a function `word_count(sentence)` that returns the number of occurrences of each word in a sentence.

24. Write a function `common_elements(list1, list2)` that returns the common elements without duplicates.

25. Write a function `merge_dict(d1, d2)` that combines two dictionaries. If a key exists in both dictionaries, add their numeric values.

26. Write a function `longest_word(sentence)` that returns the longest word in a sentence. If multiple words have the same maximum length, return the first.

27. Write a function `anagram(s1, s2)` that checks whether two strings are anagrams without using `sorted()`.

## Part 4: Lambda, Map, Filter, and Higher-Order Functions

28. Write a lambda function that returns the cube of a given number.

29. Use `map()` and a lambda function to calculate the squares of all numbers in a list.

30. Use `filter()` and a lambda function to extract numbers divisible by both 3 and 5 from a list.

31. Use `sorted()` with a lambda function to sort a list of tuples based on their second element.

    **Example input:**

    ```python
    [(1, 5), (3, 2), (4, 8), (2, 1)]
    ```

32. Write a function `apply_operation(a, b, operation)` that accepts another function as an argument and applies it to two numbers. Test it with addition, subtraction, and multiplication functions.

33. Write a function `make_multiplier(n)` that returns another function. The returned function should multiply its argument by `n`.

## Part 5: Recursion

34. Write a recursive function to calculate the factorial of a number.

35. Write a recursive function to calculate the sum of the first `n` natural numbers.

36. Write a recursive function to find the nth Fibonacci number without using loops.

37. Write a recursive function to calculate the greatest common divisor (GCD) of two positive integers using the Euclidean algorithm.

## Part 6: Real-World Problem Solving

38. **Bank Account System:** Create functions `deposit()`, `withdraw()`, and `check_balance()`. The functions should manage an account balance, prevent withdrawals exceeding the available balance, and reject invalid amounts.

39. **Student Result Management:** Write functions to calculate the total marks, percentage, and grade of a student across five subjects.

    Use the following grading rules:

    | Percentage | Grade |
    |---|---|
    | 90–100% | A+ |
    | 80–89% | A |
    | 70–79% | B |
    | 60–69% | C |
    | Below 60% | D |

40. **Password Validator:** Write a function `validate_password(password)` that checks whether a password contains:
    - At least eight characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    - One special character

    Return whether the password is valid and identify any missing requirements.

---
