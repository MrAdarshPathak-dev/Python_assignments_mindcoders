# 1. Print numbers from 1 to 10 using a for loop.  
for i in range(0,11):
    print(i)

# 2. Print numbers from 10 to 1.  
for i in range(10,0,-1):
    print(i)

# 3. Print all even numbers from 1 to 50. 
for i in range(0,51,2):
    print(i)

# 4. Print all odd numbers from 1 to 50. 
for i in range(1,51,2):
    print(i)

# 5. Print the first 20 natural numbers. 
for i in range(1,21):
    print(i)

# 6. Print the first 20 multiples of 5. 
for i in range(0,21):
    print(i*5)

# 7. Print numbers from 1 to 100, each on a separate line.
for i in range(1,101):
    print(i)

# 8. Print the numbers from 50 to 100.  
for i in range(50,101):
    print(i)

# 9. Print the squares of numbers from 1 to 10. 
#    * Expected: `1 4 9 16 25 36 49 64 81 100` 
for i in range(1,11):
    print(i**2,end=" ")

# 10. Print the cubes of numbers from 1 to 10. 
for i in range(1,11):
    print(i**3,end=" ")

# 11. Find the sum of numbers from 1 to 100.  
sum = 0
for i in range(1,101):
    sum+=i
print(sum)

# 12. Find the sum of all even numbers from 1 to 100. 
sum = 0
for i in range(0,101,2):
    sum+=i
print(sum)

# 13. Find the sum of all odd numbers from 1 to 100.
sum = 0
for i in range(1,101,2):
    sum+=i
print(sum)

# 14. Find the product of numbers from 1 to 10. 
product=1
for i in range(1,11):
    product*=i
print(product)


# 15. Take a number from the user and print its multiplication table from 1 to 10.  
num = int(input("enter number"))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

# 16. Take a number n from the user and calculate: `1 + 2 + 3 + ... + n` 
total = 0
num = int(input("enter number"))
for i in range(0,num+1):
    total+=i
print(total)

# 17. Take a number n and calculate: `1² + 2² + 3² + ... + n²` 
total = 0
num = int(input("enter number"))
for i in range(0,num+1):
    total+=i**2
print(total)

# 18. Take a number n and calculate: `1³ + 2³ + 3³ + ... + n³` 
total = 0
num = int(input("enter number"))
for i in range(0,num+1):
    total+=i**3
print(total)

# 19. Take a number from the user and calculate its factorial using a for loop.
  
num = int(input("enter number:"))
fact = 1
for i in range(num,0,-1):
    fact *= i
print(fact)

# 20. Count how many numbers between 1 and 100 are divisible by 3.
count=0
for i in range(1,101):
    if i%3==0:
        count+=1
print(count)

# 21. Print all numbers between 1 and 100 that are divisible by both 3 and 5.
count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count+=1
print(count)

# 22. Print all numbers between 1 and 100 that are divisible by 7. 
count=0
for i in range(1,101):
    if i%7==0:
        count+=1
print(count)

# 24. Count the numbers between 1 and 100 that are divisible by either 3 or 5.  
count=0
for i in range(1,101):
    if i%3==0 or i%5==0:
        count+=1
print(count)

# 25. Find the sum of all numbers between 1 and 100 that are divisible by 5.
sum=0
for  i in range(1,101):
    if i%5==0:
        sum+=i
print(sum)


# 26.  Print all numbers between 1 and 100 that are not divisible by 2.  
for i in range(1,101):
    if i%2!=0:
        print(i)

# 27. Find the largest number among: `numbers = [12, 45, 7, 89, 34, 23]` (Do not use `max()`). 
numbers = [12, 45, 7, 89, 34, 23, 99]
largest = numbers[0]
for num in numbers:
    if largest<num:
        largest=num

print(largest)

# 28. Find the smallest number in a list without using `min()`. 
numbers=[12, 45, 7, 89, 34, 23, 99]
smallest = numbers[0]
for num in numbers:
    if smallest>num:
        print(smallest)


# 29. Count how many positive, negative, and zero values are present: `numbers = [10, -5, 0, 7, -2, 0, 15, -8]` 
numbers = [10, -5, 0, 7, -2, 0, 15, -8]
negative=0
positive=0
zero=0
for num in numbers:
    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero+=1
print(f"Positive:{positive}\nNegative:{negative}\nZero:{zero}")

# 30. Find the sum of all positive numbers in a list.
numbers = [10, -5, 0, 7, -2, 0, 15, -8]
sum=0
for num in numbers:
    if num>0:
        sum+=num

print("sum of all positive integer:",sum)


# 31. Print each character of: `text = "Python"` 
text = "Python"
for ch in text:
    # print(ch,end=",")
    print(ch)

# 32. Count the number of characters in a string without using `len()`.  
text = "Python is the best."
length = 0
for ch in text:
    length+=1
print("Length:",length)

# 33. Count the number of vowels in a string.
text = "Python is the best."
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count+=1
print(count)


# 34. Count the number of consonants in a string. 

text = "Python is the best."
count=0
for ch in text:
    if ch not in "aeiouAEIOU":
        count+=1
print(count)


# 35. Count how many times the letter 'a' appears in a string.  
text = "Python is a high level language."
count = 0
for ch in text:
    if ch == "a":
        count+=1
print(count)

# 36. Print only the vowels from a given string.  
text = "Python is a high level language."
for ch in text:
    if ch in "aeiouAEIOU":
        print(ch,end=",")

# 37. Print a string in reverse using a for loop.  
text = "Python"
for i in range(len(text)-1,-1,-1):
                print(text[i],end="")

# second approach
s = "aadi"
rev = ""
for i in s:
    rev  = i+rev #concatenation
print(rev)


# 38. Count the number of uppercase and lowercase characters in a string.  
uppercase = 0
lowercase = 0
non_alphaChar=0
string = "Python Is The Best"
for ch in string:
        #ASCII VALUE OF A TO Z is 65-90
    if ord(ch)>=65 and ord(ch)<=90: 
        uppercase+=1
        #ASCII VALUE OF a TO z is 97-122
    elif ch>=97 and ch<=122:
        lowercase+=1
    else:
        non_alphaChar+=1
print(f"Uppercase:{uppercase}\nLowercase:{lowercase}\nNon Alpha Chars:{non_alphaChar}")

# 39. Count how many digits are present in a string. 
text = "MY ROLL NUMBER IS 7077"
count=0
for ch in text:
    if ch in "1234567890":
        count+=1
print(count)

# 40. Take a string and create a new string containing only the characters that are not spaces.  

string1="Python is the best"
string2=""
for ch in string1:
    if ch!=" ":
        string2+=ch
print(string2)

# 41. Find the sum of all elements in: `numbers = [10, 20, 30, 40, 50]` (Do not use `sum()`). 
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum+=num

print(sum)

# 42. Find the average of elements in a list.  
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum+=num
    avg = sum/len(numbers)

print(avg)

# 43. Find the largest element without using `max()`.
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print(largest)

# 44. Find the second-largest element in a list.  
numbers = [10, 20, 30, 40, 50]
largest = float('-inf')
second_largest = float('-inf')
for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(largest)
print(second_largest)


# 45. Count how many even and odd numbers are present in a list.
numbers = [2, 5, 2, 8, 2, 9]
even_count=0
odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Even Count:{even_count}\nOdd count:{odd_count}")

# 46. Create a new list containing only the even numbers.  
numbers=[2,4,5,6,7,8,9]
even_list = []
for num in numbers:
    if num%2==0:
        even_list.append(num)
print(even_list)

# 47. Create a new list containing only numbers greater than 50.
numbers=[24, 460, 57, 68, 72, 18, 29]
above50_list = []
for num in numbers:
    if num>50:
        above50_list.append(num)
print(above50_list)

# 48. Find the number of occurrences of a particular element.  
    # * Example: `numbers = [2, 5, 2, 8, 2, 9]` -> Count how many times 2 occurs. 
numbers = [2, 5, 2, 8, 2, 9]
print(numbers)
target = int(input("enter the element to check its occurence:"))
count = 0
for num in numbers:
    if num==target:
        count+=1
print(f"{target} occurs {count} times")

# 49. Remove duplicate elements from a list using a for loop.  
numbers = [2, 5, 2, 8, 2, 9]
unique_num=[]
for num in numbers:
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)

# 50. Reverse a list using a for loop without using `reverse()` or slicing. 
numbers = [2, 5, 2, 8, 2, 9]
reverse_list = []
for i in range(len(numbers)-1,-1,-1):
    reverse_list.append(numbers[i])
print(reverse_list)



# 51. Take a number and determine whether it is prime using a for loop.  
number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime Number")
else:
    print("not a prime number")


# 52. Print all prime numbers between 1 and 100.
for i in range(1,101):
    is_prime=True
    for j in range(2,i):
        if i % j == 0:
            is_prime=False
            break
    else:
        print(i)

# 53. Count the number of prime numbers between 1 and 100.
count = 0
for i in range(1,101):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    else:
        count+=1
print(count)

# 54. Take a number and print all its factors.  
#     * Example: 
#       Input: 12 
#       Output: 1 2 3 4 6 12 
# 54. Take a number and print all its factors.  
#     * Example: 
#       Input: 12 
#       Output: 1 2 3 4 6 12 
num = int(input("enter number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")

# 55. Find the GCD/HCF of two numbers using a for loop.  
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
factors=[]
for i in range(1,min(num1,num2)+1):
    if num1%i==0 and num2%i==0:
        factors.append(i)
print("Common Factors:",factors)
print(f"GCD of {num1} and {num2}:{max(factors)}")


# 56. Find the LCM of two numbers using a for loop.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(max(num1, num2), (num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        break

# 57. Check whether a number is a perfect number.  
number = int(input("Enter number:"))
sum = 0
for num in range(1,number):
    if number%num==0:
        sum+=num
if sum==number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

# 58. Print all perfect numbers between 1 and 1000.
for i in range(1,1001):
    total = 0
    for j in range(1,i):
        if i%j==0:
            total+=j
    if total == i:
        print(i,end=", ")

# 59. Check whether a number is an Armstrong number. 
number = input("Enter number:")
sum = 0
order = len(number)
for digits in number:
    digits = int(digits)
    powered_digit=(digits**order)
    sum+=powered_digit
if int(number)==sum:
    print(f"{number} is a Armstrong number")
else:
    print(f"{number} is not a armstrong number")



# 60. Print all Armstrong numbers between 1 and 1000.  
for i in range(1, 1001):
    total = 0
    number = str(i)
    order = len(number)

    for digit in number:
        digit = int(digit)
        powered_digit = digit**order
        total += powered_digit

    if i == total:
        print(i,"is armstrong number")


#========================================================================================# Questions 61-70: Pattern programs are in patterns.py==========================================


# ===================Questions from question.md after pattern=======================================================================



# 71. Find the second-smallest number in a list without using `sort()`.  
numbers = [4,6,8,8,9,5,3]
smallest = float('inf')
second_smallest = float('inf')
for  num in numbers:
    if num<smallest:
        second_smallest=smallest
        smallest=num
    elif num<second_smallest and num!=smallest:
        second_smallest = num
print(f"smallest:{smallest} and second smallest: {second_smallest}")

# 72. Find all pairs of numbers whose sum is 10.  
for i in range(0,10):
    for j in range(0,10):
        if i+j==10:
            print(f"({i},{j})")

# 73. Find the frequency of every element in a list.  
number = [1, 2, 4, 1, 1, 4, 5, 3, 2]

for i in number:
    count = 0
    for j in number:
        if i==j:
            count+=1
    print(f"{i} --> {count} times")

# 74. Find the character that occurs most frequently in a string.  
string = input("enter a string: ")
max_char = ""
max_count = 0
for i in string:
    count = 0
    for j in string:
        if i==j:
            count+=1
    if count > max_count:
        max_count = count
        max_char = i
print(f"{max_char} --> {max_count} times")

# 75. Check whether a string is a palindrome using a for loop.
string = input("enter a string: ")
rev_str =""
for char in string:
    rev_str=char+rev_str
if string==rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")

# 76. Find all numbers between 1 and 100 that are both prime and odd.  
for i in range(1,101):
    isPrime = True
    for j in range(2,i):
        if i%j == 0:
            isPrime = False
            break
    if isPrime and i%2!=0:
        print(i,"is prime and odd")

# 77. Generate the first n terms of the Fibonacci series using a for loop.
a = 0
b = 1
n = int(input("enter the value of n:"))
if n == 1:
    print(a)
else:
    print(a,end=", ")
    print(b,end=", ")
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c,end=", ")


# 78. Check whether a number belongs to the Fibonacci sequence. 
import itertools
number = int(input("Enter number to check if it belongs to the Fibonacci sequence: "))
a = 0
b = 1
if number<0:
    print("Does not belong to fabonacci sequence.")
elif number == 0:
    print("0 belongs to fabonacci sequence")
else:
    for i in itertools.count(2):
        if a == number:
            print(f"{number} belongs to fabonacci sequence")
            break
        elif a > number:
            print(f"{number} doesn't belong to fabonacci sequence")
            break
        
        else:
            c = a + b
            a = b
            b = c


    
# 79. Find the digital sum of a number using a for loop.  
number = input("Enter a number: ")
total = 0

for digit in number:
    total += int(digit)

print("Digital sum:", total)


# 80. Convert a decimal number to binary using a for loop.

number = int(input("Enter a number: "))
binary = ""

if number == 0:
    binary = "0"
else:
    for i in range(number.bit_length()): 
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

print("Binary:", binary)