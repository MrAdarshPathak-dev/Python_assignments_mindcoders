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

