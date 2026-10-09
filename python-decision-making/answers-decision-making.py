# Q1. Positive Number
# Write a Python program to input a number and check whether it is positive.
num=int(input("enter a number:"))
if num<0:
    print(f"{num} is negative integer")
elif num>0:
    print(f"{num} is positive integer")
else:
    print(f"{num} is neither negative nor positive.")

#===============================================================
# Q2. Even Number
# Write a program to input a number and check whether it is even.
num=int(input("enter a number:"))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd")

#===============================================================
# Q3. Voting Eligibility
# Input a person's age and check whether they are eligible to vote.
age = int(input("enter your age:"))
if age>0 and age<18:
    print("not eligible")
elif age>=18 and age<100:
    print("eligible")
else:
    print("enter a valid age!!!")

# Q4. Greater Than 100
# Input a number and check whether it is greater than 100.
number=int(input("enter a number:"))
if num > 100:
    print(f"{num} is greater than 100")
else:
    print(f"{num} is less than 100")

#Q5. Divisible by 5
# Input a number and check whether it is divisible by 5.
number=int(input("enter a number:"))
if num%5==0:
    print(f"{number} is divisible by 5")
else:
    print(f"{number} is not divisible by 5")

# Q6. Even or Odd
# Write a program to determine whether a number is even or odd.
num=int(input("enter a number:"))
if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd")

# Q7. Positive or Negative
# Input a number and display whether it is positive or negative.
num=int(input("enter a number:"))
if num<0:
    print(f"{num} is negative integer")
elif num>0:
    print(f"{num} is positive integer")
else:
    print(f"{num} is neither negative nor positive.")

# Q8. Pass or Fail
# Input marks. If marks are 40 or above, print `Pass`; otherwise print `Fail`.
marks = int(input("Enter marks:"))
if marks>=40 and marks<101:
    print("Pass")
else:
    print("fail")

# Q9. Largest of Two Numbers
# Input two numbers and display the larger number.
num1=print("enter the first number:")
num2=print("enter the second number:")
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num2} and {num1} are equal.")

# Q10. Eligible for Driving License
# Input age and apply the following rule:
# * Age ≥ 18 → `Eligible`
# * Otherwise → `Not eligible`
age = int(input("enter your age:"))
if age>0 and age<18:
    print("not eligible")
elif age>=18 and age<100:
    print("eligible")
else:
    print("enter a valid age!!!")

# Q11. Grade Calculator
# Input marks and display the corresponding grade based on this schema:

# | Marks | Grade |
# | :--- | :--- |
# | 90–100 | A |
# | 80–89 | B |
# | 70–79 | C |
# | 60–69 | D |
# | Below 60 | F |

marks = int(input("Enter marks:"))
if marks >=90 and  marks <=100:
    print("A")
elif marks >=80 and  marks <=89:
    print("B")
elif marks >=70 and  marks <=79:
    print("C")
elif marks >=60 and  marks <=69:
    print("D")
else:
    print("F")

# Q12. Temperature Classification
# Input temperature and display its classification:
# * **Above 40** → `Very Hot`
# * **30–40** → `Hot`
# * **20–29** → `Normal`
# * **10–19** → `Cold`
# * **Below 10** → `Very Cold`
temp=int(input("enter temperature"))
if temp > 40:
    print("Very Hot")
elif temp >=30 and  temp <=40:
    print("Hot")
elif temp >=20 and  temp <=29:
    print("Normal")
elif temp >=10 and  temp <=19:
    print("Cold")
else:
    print("Very Cold")

# Q14. Day Number
# Input a number from 1 to 7 and display the corresponding day:
# * `1` → Monday, `2` → Tuesday, `3` → Wednesday, ..., `7` → Sunday.
# * If the user enters anything outside 1–7, display `Invalid day`.
day=int(input("Input day number from 1 to 7"))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

# Q15. Month Classification
# Input a month number and display the season:
# * `12, 1, 2` → Winter
# * `3, 4, 5` → Spring
# * `6, 7, 8` → Summer
# * `9, 10, 11` → Autumn
month=int(input("Enter month number from 1 to 12:"))
if month==12 or month==1 or month==2:
    print("Winter")
elif month==3 or month==4 or month==5:
    print("Spring")
elif month==6 or month==7 or month==8:
    print("Spring")
elif month==9 or month==10 or month==11:
    print("Spring")
else:
    print("Invalid month")

# Q16. Largest of Three Numbers
# Input three numbers and find the largest using decision-making statements.
# * **Example:**
#   * **Input:** `25`, `48`, `17`
#   * **Output:** `48 is the largest`
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1<num2 and num3<num2:
    print(f"{num2} is the largest.")
elif num1<num3 and num2<num3:
    print(f"{num3} is the largest.")
else:
    print(f"{num1} is the largest.")

# Q17. Smallest of Three Numbers
# Input three numbers and find the smallest number.
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
if num1>num2 and num3>num2:
    print(f"{num2} is the smallest.")
elif num1>num3 and num2>num3:
    print(f"{num3} is the smallest.")
else:
    print(f"{num1} is the smallest.")

#  Q18. Leap Year
# Write a program to determine whether a year is a leap year.
# * **Hint:** A year is a leap year if it is divisible by 400 **OR** divisible by 4 but not by 100.
year=int(input("enter the year:"))
if year%400==0:
    print("leap year.") 
elif year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Not a Leap year.")

# Q19. Divisibility Test
# Input a number and determine whether it is:
# * Divisible by both 3 and 5
# * Divisible only by 3
# * Divisible only by 5
# * Divisible by neither
number=int(input("enter a number:"))
if number%3==0 and number%5==0:
    print("Divisible by both 3 and 5")
elif number%3==0 and number%5!=0:
    print("Divisible only by 3")
elif number%3!=0 and number%5==0:
    print("Divisible only by  5")
else:
    print("Divisible by neither")

# Q20. Electricity Bill
# Calculate the electricity bill according to the following progressive rules:

# | Units | Rate |
# | :--- | :--- |
# | 0–100 | ₹5/unit |
# | 101–200 | ₹7/unit |
# | 201–300 | ₹10/unit |
# | Above 300 | ₹15/unit |
units=int(input("enter your electricity units:"))
if units>=0 and units<=100:
    bill=units*5
    print("Bill:",bill)
elif 101<=units and units<=200:
    bill=units*7
    print("Bill:",bill)
elif 201<=units and units<=300:
    bill=units*10
    print("Bill:",bill)
else:
    bill=units*15
    print("Bill:",bill)

# . Nested `if` & Complex Logic

#  Q21. Login System
# Create a simple login program.
# * **Input:** `Username`, `Password`
# * **Rules:**
#   * Username must be `"admin"`.
#   * If username is correct, check the password.
#   * Password must be `"1234"`.
#   * Display specific, appropriate messages for an incorrect username versus an incorrect password.
username="admin"
password="1234"
entered_username=input("Enter your user name:")
entered_password=input("Enter your password:")
if entered_username==username :
    if entered_password!=password:
        print("Wrong password!")
    else:
        print("Successfully logged in!")
else:
    print("Incorrect Username!")

# Q22. ATM Withdrawal
# Given an initial state of `balance = 10000`, input a withdrawal amount.
# * **Rules:**
#   * Amount must be greater than 0.
#   * Amount must be a multiple of 100.
#   * Amount must not exceed the current balance.
#   * Otherwise, display appropriate validation error messages.

balance = 10000
print(''' **Instructions:**
Amount must be greater than 0.
Amount must be a multiple of 100.
Amount must not exceed the current balance.''')
withdrawal=int(input("Enter the amount want to withdraw:"))
if withdrawal > 0 and withdrawal % 100 == 0:
    if withdrawal<=balance:
        balance=balance-withdrawal
        print("Transaction successful! current bal.",balance)
    else:
        print("Transaction failed!!! Low balance.")
else:
    print("Please follow the instructions.")

# Q23. College Admission
# Input `percentage` and `entrance_exam_score`. Admission is allowed only if:
# * Percentage ≥ 60 **AND** entrance score ≥ 50.
# * Otherwise, display the specific reason why the admission was rejected.

percentage=int(input("Enter your Percentage:"))
entrance_exam_score=int(input("Enter your Entrance Exam Score: "))
if percentage>=60 and entrance_exam_score>=50:
        print("Eligible for the Admission")
else:
     print("Admission Rejected due to the following reason(s):")
     if percentage < 60:
        print("- Low percentage (Must be ≥ 60%)")
        
     if entrance_exam_score < 50:
        print("- Low entrance exam score (Must be ≥ 50)")

# Q24. Shopping Discount
# Input the total purchase amount and calculate the final amount after applying discounts:
# * Amount ≥ ₹10,000 → 20% discount
# * Amount ≥ ₹5,000 → 10% discount
# * Amount ≥ ₹2,000 → 5% discount
# * Below ₹2,000 → No discount
amount = int(input("Enter total purchase amount:"))
if amount >= 10000:
    discount=amount*0.20
    amount=amount-discount
    print("Total amount after Discount:",amount)
elif amount>=5000 and amount < 10000:
    discount=amount*0.10
    amount=amount-discount
    print("Total amount after Discount:",amount)
elif amount>=2000 and amount < 5000:
    discount=amount*0.05
    amount=amount-discount
    print("Total amount after Discount:",amount)
else:
    print("No discount!Total amount",amount)

# Q25. Triangle Classification
# Input three sides of a triangle (a, b, c).
# 1. First determine whether the sides can form a valid triangle. 
#    * *Hint:* Must satisfy a + b > c, b + c > a, and a + c > b.
# 2. If valid, classify it as: `Equilateral`, `Isosceles`, or `Scalene`.
a=int(input("enter first side of triangle"))
b=int(input("enter second side of triangle"))
c=int(input("enter third side of triangle"))
if a + b> c or b + c > a or a + c > b:
    if a==b and b==c:
        print("Equilateral Triangle")
    elif a==b or a==c or b==c:
        print("Isosceles Triangle")
    else:
        print("Scalene")

# Q26. Profit or Loss
# Input `Cost Price` and `Selling Price`. Calculate and display whether it results in a Profit, Loss, or No profit/no loss. Include the calculated profit or loss percentages where applicable.
cp = int(input("enter cost price:"))
sp = int(input("enter selling price:"))
if cp>sp:
    loss = cp - sp
    lossPercent = (loss*100)/cp
    print(f"Loss:{loss}\nLoss Percentage:{lossPercent}%")
elif sp>cp:
    profit = sp - cp
    profitPercent = (profit*100)/cp
    print(f"Profit:{profit}\nProfit Percentage:{profitPercent}%")
else:
    print("Neither profit nor loss")