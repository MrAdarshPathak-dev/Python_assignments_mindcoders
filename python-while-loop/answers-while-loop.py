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
