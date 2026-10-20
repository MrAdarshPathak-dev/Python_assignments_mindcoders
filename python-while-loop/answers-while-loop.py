# Q1. Write a program using a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1

# 2. **Print numbers from 10 to 1**
#    Print numbers in reverse order using a while loop.
i=10
while i>=1:
    print(i)
    i-=1


# 3. **Print even numbers**
#    Print all even numbers from 1 to 20.
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1


# 4. **Print odd numbers**
#    Print all odd numbers from 1 to 20.
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i+=1

# 5. **Print multiples**
#    Ask the user for a number and print its first 10 multiples.
num = int(input("enter a number:"))
i=1
while i<=10:
    print(num*i)
    i+=1


# 6. **Sum of numbers**
#    Find the sum of numbers from 1 to 100 using a while loop.
i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

# 7. **Count numbers**
#    Ask the user for a number n and count from 1 to n.
number = int(input("enter number:"))
i=1
while i<=number:
    print(i,end=" ")
    i+=1

# 8. **Positive or negative input**
#    Keep asking the user to enter a number until they enter 0.
while True:
    number = int(input("enter a number:"))
    if number == 0:
        print("exited successfully")
        break

# 9. **Password validation**
#    Keep asking for a password until the user enters the correct password.
while True:
    password = input("enter password:")
    if password=="Admin12":
        print("Correct password")
        break
    else:
        print("Wrong password!!! try again.")

# 10. **Limited attempts**
    # Give the user 3 attempts to enter the correct password.
attempts = 3
while attempts>=0:
    password = input("enter password:")
    if password=="Admin12":
        print("Correct password")
        break
    else:
        attempts-=1
        print(f"Wrong password!!! try again. {attempts} left")
        print("Account blocked!!!")

# 11. **Keep asking for numbers**
#     Keep taking numbers from the user and stop when they enter "-1." At the end, display the sum of all entered numbers.

total=0
while True:
    print("To exit enter -1")
    number = int(input("enter number:"))
    if number == -1:
        break
    else:
        total+=number
print(total)

# 12. **Count positive numbers**
#  Keep accepting numbers until the user enters 0. Count how many positive numbers were entered.
count=0
while True:
    number = int(input("enter number:"))
    if number == 0:
        break
    else:
        if number>=0:
            count+=1
print(f"you entered {count} positive number")


# 13. **Largest number**
#     Keep accepting numbers until the user enters 0. Find the largest number entered.
largest = float('-inf')
while True:
    number = int(input("enter number:"))
    if number == 0:
        break
    else:
        if number>largest:
            largest=number
print("largest : ",largest)

# 14. **Smallest number**
#     Keep accepting numbers until the user enters 0. Find the smallest number entered.
smallest = float('inf')
while True:
    number = int(input("enter number:"))
    if number == 0:
        break
    else:
        if number<smallest:
            smallest=number
print("smallest : ",smallest)

# 15. **Factorial**
#     Ask the user for a number and calculate its factorial using while.
n = int(input("enter number:"))
fact = 1
i = 1
while i<=n:
    fact *= i
    i+=1
print(fact)

# 16. **Sum of digits**
#     Input a number such as 5832 and calculate: 5 + 8 + 3 + 2 = 18
n = (input("Enter a number: "))
total = 0
i = 0
while i<=len(n)-1:
    digit = n[i]
    digit = int(digit)
    total += digit
    i+=1
print(total)

# 17. **Count digits**
#     Count how many digits are present in a number.
n = (input("Enter a number: "))
count = 0
i = 0
while i<=len(n)-1:
    count+=1
    i+=1
print(count)


# 18. **Reverse a number**
#     Input: 12345
#     Output: 54321
n = input("Enter a number:")
rev_n=""
i = 0
while i<=len(n)-1:
    rev_n = n[i] + rev_n
    i+=1
print(rev_n)


# another aaproach
n = int(input("Enter number:"))
rev_n=0
i=0
while n>0:
    remiander = n%10
    rev_n=(rev_n*10) + remiander
    n = n // 10
print(rev_n)

# 19. **Palindrome number**
#     Check whether a number is a palindrome.
#     * 121 → Palindrome
#     * 123 → Not Palindrome
n = input("Enter a number:")
rev_n=""
i = 0
while i<=len(n)-1:
    rev_n = n[i] + rev_n
    i+=1
if rev_n==n:
    print(f"{n}: Palindrome")
else:
    print(f"{n}: Not Palindrome")

#mathematical approach
n = int(input("Enter number:"))
number = n
rev_n=0
i=0
while n>0:
    remiander = n%10
    rev_n=(rev_n*10) + remiander
    n = n // 10
if rev_n==number:
    print(f"{number}: Palindrome")
else:
    print(f"{number}: Not Palindrome")

# 20. **Multiplication table**
#     Ask for a number and print its multiplication table using while.
n = int(input("Enter a number:"))
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1


# 21. **Power calculation**
#     Calculate x^y using a while loop without using the exponentiation operator (**).
number = int(input("Enter the base number: "))
power = int(input("Enter the exponentiation power: "))
i=0
result = 1
while i < power:
    result *= number
    i+=1
print(result)



# 22. **Prime number**
#     Check whether a given number is prime using a while loop.
n = int(input("enter a number:"))
i=2
isPrime = False
while i<n:
    if n%i==0:
        print(n,"Not prime")
        break
    else:
        i+=1
        isPrime = True

if isPrime:
    print(n," --> Prime")



# 23. **Print prime numbers**
#     Print all prime numbers between 1 and 100 using while loops.
isPrime = True
i=1
while i<=100:
    j=2
    while j<i:
        if i%j==0:
            isPrime = False
            # print(n,"Not prime")
            break
        else:
            isPrime = True
            j+=1
    
    if isPrime:
        print(i,end=" ")
    i+=1

# 24. **Guess the number**
#     Store a secret number and keep asking the user to guess until they guess correctly.
secret_number = 7
while True:
    guess = int(input("Enter the secret number (1 to 10):"))
    if guess == secret_number:
        print("Right guess!")
        break
    else:
        print("Wrong guess! Try again.")


# 25. **Number guessing with hints**
#     * Enter guess: 30 -> Too high!
#     * Enter guess: 15 -> Too low!
#     * Enter guess: 20 -> Correct!
import random
secret_number = random.randint(1,10)
while True:
    guess = int(input("Enter the secret number (1 to 10):"))
    if guess > secret_number:
        print("Too high!")
        
    elif guess < secret_number:
        print("Too low!")

    else:
        print("Correct!")
        break

# 26. **Number guessing with attempts**
#     Give the user only 5 attempts to guess the number.
import random
i = 0 
secret_number = random.randint(1,10)
while i <= 5:
    guess = int(input("Enter the secret number (1 to 10):"))
    if guess > secret_number:
        print(f"Too high! {5-i} attempt remaining")
            
    elif guess < secret_number:
        print(f"Too low! {5-i} attempt remaining.")
    
    else:
        print("Correct!")
        break

    i+=1

# 27. **Menu-driven calculator**
#     Display: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit
#     Keep displaying the menu until the user chooses 5.
def input_numbers():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    return num1,num2
while True:
    print('''MENU:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit''')
    
    user_input = int(input("Choose from menu (1-5): "))
    if user_input == 1:
        num1,num2 = input_numbers()
        print(f"Additon :{num1} + {num2} = {num1+num2}")
    elif user_input == 2:
        num1,num2 = input_numbers()
        print(f"Subtraction: {num1} - {num2} = {num1-num2}")
    elif user_input == 3:
        num1,num2 = input_numbers()
        print(f"Multiplication: {num1} * {num2} = {num1*num2}")
    elif user_input == 4:
        num1,num2 = input_numbers()
        print(f"Division: {num1} / {num2} = {num1/num2}")
    elif user_input == 5:
        break
    else:
        print("Choose Valid Option:")
        
    
# 28. **Simple ATM**
#     Create a program with: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit        
balance = 10000

while True:
    print('''MENU:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit''')
    user_input = int(input("Choose from menu (1-4): "))
    if user_input == 1:
        print("Balance:",balance)
    elif user_input == 2:
        deposit_amount = int(input("Enter Your Deposit Amount: "))
        if deposit_amount<=0:
            print("Invalid Transaction!")
        else:
            balance+=deposit_amount
            print("Transaction Succeful! Avl Bal. ",balance)
    elif user_input == 3:
        withdrawal_amount = int(input("Enter Your Withdrawal Amount: "))
        if withdrawal_amount<=0:
            print("Invalid Transaction!")
        elif withdrawal_amount >balance:
            print("Transaction Failed!!! Insufficient Balance: ")
        else:
            balance-=withdrawal_amount
            print("Transaction Succeful! Avl Bal. ",balance)

    elif user_input == 4:
        print("Exited!")
        break
    else:
        print("Choose Valid Option:")


# 29. **Login system**
#     Ask for username and password. Allow the user to try until the correct credentials are entered.
username = "@admin1"
password = "admin1"
while True:
    enter_name = input("Enter your username: ")
    if enter_name == username:
        enter_pass = input("Enter your password: ")
        if enter_pass == password:
            print("Login successful")
            break
        else:
            print("wrong password! Try again...")
    else:
        print("Wrong username! Try again...")

# 30. **Continue or stop**
#     Ask the user: Do you want to continue? (yes/no) Repeat the program while the answer is "yes".
i = 1

while True:
    print(i)
    user_choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if user_choice == "yes":
        i += 1
    elif user_choice == "no":
        print("Program stopped.")
        break
    else:
        print("Invalid input! Please type 'yes' or 'no'.")


# 31. **Fibonacci series**
#     Print: 0 1 1 2 3 5 8 13 21 34 using a while loop.

a = 0
b = 1
n = int(input("Enter a number:"))
i = 0
print(a,end=" ")
print(b,end=" ")
while i<=n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1

# 32. **Armstrong number**
#     Check whether a number is an Armstrong number. Example: 153 = 1³ + 5³ + 3³

n = input("Enter a number: ")
i = 0
order = len(n)
total = 0
while i<order:
    digit = n[i]
    digit = int(digit)
    powered_digit = digit**order
    total += powered_digit
    i+=1
if total == int(n):
    print("Armstrong number!")
else:
    print("Not an armstrong number!")


# 33. **Perfect number**
#     Check whether a number is a perfect number. Example: 6 → 1 + 2 + 3 = 6
i = 1
n = int(input("Enter a number: "))
total = 0
while i<n:
    if n%i==0:
        total += i
    i+=1
if total == n:
    print("Perfect number")
else:
    print("Not a perfect number")
    
# 34. **GCD**
#     Find the Greatest Common Divisor of two numbers using a while loop.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
i = 1
gcd = 1 
while i<=num1:
    if num1%i == 0 and num2%i==0:
        gcd = i
    i+=1
print("Greatest Common Divisor is:", gcd)

# 35. **LCM**
#     Find the Least Common Multiple of two numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
lcm = 1
i = num1
while True:
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
    i+=1
print("Least Common Multiple: ",lcm)

# 36. **Decimal to binary**
    # Convert a decimal number to binary using a while loop.









# 38. **Pattern using while**
#     Print:
#     *
#     **
#     ***
#     ****
#     *****
i = 1
while i<=5:
    j = 1
    while j <= i:
        print("*",end="")
        j+=1
    print()
    i+=1

# 39. **Number pattern**
#     Print:
#     1 
#     12 
#     123 
#     1234 
#     12345 
#     using while.
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1

# 40. **Interactive student marks program**
#     Keep accepting marks for students until the user enters "-1." At the end display:
#     * Number of students
#     * Total marks
#     * Average marks
#     * Highest marks
#     * Lowest marks
