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

### Q27. BMI Category
# Input `weight` (in kg) and `height` (in meters). Calculate BMI = weight / height² and classify:

# | BMI | Category |
# | :--- | :--- |
# | < 18.5 | Underweight |
# | 18.5–24.9 | Normal |
# | 25–29.9 | Overweight |
# | ≥ 30 | Obese |
weight=int(input("Enter your weight in kg"))
height = int(input("Enter your height in meters"))
bmi = weight/(height**2)
print(f"Your BMI:{bmi}")
if bmi < 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >=25 and bmi <29.9:
    print("Overweight")
else:
    print("Obese")

### Q28. Calculator
# Input two numbers and an operator (`+`, `-`, `*`, `/`). Perform the operation using `if-elif-else`. Explicitly handle and prevent division by zero errors.
# * **Example:**
#   * **Input:** `10`, `5`, `*`
#   * **Output:** `50`
num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
operator = input("Select an operator among: + - * / : ")
if operator=="+":
    sum = num1+num2
    print(f"{num1} + {num2} = {sum}")
elif operator=="-":
    subs = num1-num2
    print(f"{num1} - {num2} = {subs}")
elif operator=="*":
    multiply = num1*num2
    print(f"{num1} * {num2} = {multiply}")
elif operator=="/":
    if num2==0:
        print("Undefined operation")
    else:
        divide = num1+num2
        print(f"{num1}/{num2}={divide}")
else:
    print("please choose valid operator")

### Q29. Employee Bonus
# Input `salary` and `years_of_service`. Calculate the bonus amount and final salary based on these rules:
# * Service ≥ 10 years → 20% bonus
# * Service ≥ 5 years → 10% bonus
# * Service ≥ 2 years → 5% bonus
# * Otherwise → No bonus

salary =int(input("enter your salary: "))
years_of_service = int(input("enter years of service: "))
if years_of_service>=10:
    bonus = salary*(20/100)
    print("Salary + Bonus:",salary+bonus)
elif years_of_service>=5 and years_of_service<10:
    bonus = salary*(10/100)
    print("Salary + Bonus:",salary+bonus)
elif years_of_service>=2 and years_of_service<5:
    bonus = salary*(5/100)
    print("Salary + Bonus:",salary+bonus)
else:
    print("No bonus!!! Salary:",salary)


### Q30. ATM Menu
# Create an ATM program that accepts an operation input choice:
# * `1` → Check Balance
# * `2` → Deposit
# * `3` → Withdraw
# * `4` → Exit
# Use decision statements to execute the operation. Ensure a validation check handles sufficient balance for withdrawals.
balance = 0

print('''Menu:
 `1` → Check Balance
 `2` → Deposit
 `3` → Withdraw
 `4` → Exit''')
input_choice = int(input("choose any option to perform any operation:"))
if input_choice==1:
    print("current balance:",balance)

elif input_choice==2:
    deposit_amount = int(input("Enter your deposit amount:"))
    if deposit_amount <= 0:
        print("invalid operation!!! Current balance:",balance)
    elif deposit_amount > 0:
        balance+=deposit_amount
        print("Transaction Successful! Current balance:",balance)

elif input_choice==3:
    withdrawal_amount = int(input("Enter your Withdrawal amount:"))
    if withdrawal_amount <= 0:
        print("invalid operation!!! Current balance:",balance)
    elif balance< withdrawal_amount:
        print("insufficiant balance! Current Balance:",balance)
    else:
        balance-=withdrawal_amount
        print("Transaction Successful! Current balance:",balance)

else:
    print("Exited")
    

### Q31. Electricity Bill with Surcharge
# Calculate a tiered slab electricity bill (using rules from Q20), then apply a surcharge:
# * If base bill > ₹5,000 → add 10% surcharge
# * If base bill > ₹10,000 → add 15% surcharge
# * **Display format:** `Units consumed`, `Base bill`, `Surcharge`, and `Final bill`. 
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

if bill > 5000  and bill <10000:
        surcharge = "10%"
        final_bill = bill + (bill*(1/10))
        print(f'''Base bill:{bill}
Surcharge:{surcharge}
Final bill:{final_bill}
''')


elif bill > 10000 :
    surcharge = "15%"
    final_bill = bill + (bill*(1/15))
    print(f'''Base bill:{bill}
Surcharge:{surcharge}
Final bill:{final_bill}
''')

else:
    surcharge = "0%"
    final_bill = bill
    print(f'''Surcharge:{surcharge}
Final bill:{final_bill}
Final bill:{bill}''')

### Q32. Student Result System
# Input individual marks for four subjects: `Python`, `SQL`, `Mathematics`, and `Statistics`.
# * **Rules:**
#   * Minimum 40 marks required in **every** subject to `Pass`; otherwise `Fail`.
#   * Calculate overall percentage and assign a grade based on the percentage if they pass.

marks={
    "Python" : int(input("Enter python marks:")),
    "SQL" : int(input("Enter SQL marks:")),
    "Mathematics" : int(input("Enter Mathematics marks:")),
    "Statistics" : int(input("Enter Statistics marks:"))
}
if (
    marks["Python"]>=40 
    and marks["SQL"]>=40 
    and marks["Mathematics"]>=40 
    and marks["Statistics"]>=40
    ):
    print("Pass")
    total = marks["Python"]+marks["SQL"]+marks["Mathematics"]+marks["Statistics"]
    percentage = float((total/400)*100) 
    print("Percentage:",percentage)
    if percentage>=90 and percentage<=100:
        print("Grade: A+")
    elif percentage>=80 and percentage<90:
        print("Grade: A")
    elif percentage>=70 and percentage<80:
        print("Grade: B")
    elif percentage>=60 and percentage<70:
        print("Grade: C")
    elif percentage>=50 and percentage<60:
        print("Grade: D")
    else:
        print("Grade: E")

else:
    print("Fail!")



### Q33. Income Tax Calculator
# Input annual income and calculate tax liability using regional income tax slabs. The program must explicitly output: `Income`, `Tax`, and remaining `Net income`.
#
# New Tax Regime Slabs (AY 2026-27 / FY 2025–26)

# • Up to ₹4,00,000: Nil (0%)
# • ₹4,00,001 – ₹8,00,000: 5%
# • ₹8,00,001 – ₹12,00,000: 10%
# • ₹12,00,001 – ₹16,00,000: 15%
# • ₹16,00,001 – ₹20,00,000: 20%
# • ₹20,00,001 – ₹24,00,000: 25%
# • Above ₹24,00,000: 30%
annual_income = int(input("Enter your annual income:"))
if annual_income>=2400000:
    tax_percent = 30
    income_tax = float(annual_income*(30/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
    
elif annual_income>=2000001 and annual_income<2400000:
    tax_percent = 25
    income_tax = float(annual_income*(25/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
elif annual_income>=1600001 and annual_income<=2000000:
    tax_percent = 20
    income_tax = float(annual_income*(20/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
elif annual_income>=1200001 and annual_income<=1600000:
    tax_percent = 15
    income_tax = float(annual_income*(15/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
elif annual_income>=800001 and annual_income<=1200000:
    tax_percent = 10
    income_tax = float(annual_income*(10/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
elif annual_income>=400001 and annual_income<=800000:
    tax_percent = 5
    income_tax = float(annual_income*(5/100))
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )
else:
    tax_percent = 0
    income_tax = 0
    net_income = annual_income - income_tax
    print(
f'''Gross Income: {annual_income}
Tax Percent: {tax_percent}
Tax: {income_tax}
Net Income: {net_income}'''
    )




### Q34. Login with Account Status
# Input `username`, `password`, and `account_status`.
# * **Rules:**
#   * Correct username → check password.
#   * Correct password → check account status.
#     * If status is `"active"` → Login successful.
#     * If status is `"blocked"` → Account blocked.
#   * Wrong credentials at any stage → Login failed.
username = input("Enter your username: ")

if username == "@Admin1":
    password = input("Enter password: ")

    if password == "admin1":
        account_status = input("Enter account status: ")

        if account_status == "active":
            print("Login Successful!")
        elif account_status == "blocked":
            print("Account blocked. Login Failed!")
        else:
            print("Login failed!")
    else:
        print("Wrong password. Login failed!")
else:
    print("Wrong username. Login failed!")



### Q35. Number Property Checker
# Input an integer and determine all of its matching attributes simultaneously:
# * Positive / negative / zero
# * Even / odd
# * Divisible by 3 / divisible by 5 / divisible by both 3 and 5 / divisible by neither

number = int(input("enter a number:"))
#block 1 Positive / negative / zero
if number > 0 :
    print(number," is positive")
elif number < 0 :
    print(number," is negative")
else:
    print(number," is zero")

#Block 2  Even / odd
if number%2 == 0:
    print(number," is even")
else:
    print(number," is odd")

# Block 3  Divisible by 3 / divisible by 5 / divisible by both 3 and 5 / divisible by neither

if number % 3 == 0 and number % 5 == 0:
    print(number," is divisible by both 3 and 5")
elif number % 3 == 0:
    print(f"{number} is divisible by 3")
elif number % 5 == 0:
    print(f"{number} is divisible by 5")
else:
    print(number, "is divisible by neither 3 nor 5")