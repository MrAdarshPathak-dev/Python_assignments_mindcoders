# Python Decision-Making Coding Questions

## 1. Basic `if` Statements

### Q1. Positive Number
Write a Python program to input a number and check whether it is positive.
* **Example:**
  * **Input:** `15`
  * **Output:** `Positive number`

### Q2. Even Number
Write a program to input a number and check whether it is even.

### Q3. Voting Eligibility
Input a person's age and check whether they are eligible to vote.

### Q4. Greater Than 100
Input a number and check whether it is greater than 100.

### Q5. Divisible by 5
Input a number and check whether it is divisible by 5.

---

## 2. `if-else` Statements

### Q6. Even or Odd
Write a program to determine whether a number is even or odd.

### Q7. Positive or Negative
Input a number and display whether it is positive or negative.

### Q8. Pass or Fail
Input marks. If marks are 40 or above, print `Pass`; otherwise print `Fail`.

### Q9. Largest of Two Numbers
Input two numbers and display the larger number.

### Q10. Eligible for Driving License
Input age and apply the following rule:
* Age ≥ 18 → `Eligible`
* Otherwise → `Not eligible`

---

## 3. `if-elif-else` Statements

### Q11. Grade Calculator
Input marks and display the corresponding grade based on this schema:

| Marks | Grade |
| :--- | :--- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

### Q12. Temperature Classification
Input temperature and display its classification:
* **Above 40** → `Very Hot`
* **30–40** → `Hot`
* **20–29** → `Normal`
* **10–19** → `Cold`
* **Below 10** → `Very Cold`

### Q13. Number Classification
Input a number and display whether it is:
* `Positive`
* `Negative`
* `Zero`

### Q14. Day Number
Input a number from 1 to 7 and display the corresponding day:
* `1` → Monday, `2` → Tuesday, `3` → Wednesday, ..., `7` → Sunday.
* If the user enters anything outside 1–7, display `Invalid day`.

### Q15. Month Classification
Input a month number and display the season:
* `12, 1, 2` → Winter
* `3, 4, 5` → Spring
* `6, 7, 8` → Summer
* `9, 10, 11` → Autumn

---

## 4. Multiple Conditions

### Q16. Largest of Three Numbers
Input three numbers and find the largest using decision-making statements.
* **Example:**
  * **Input:** `25`, `48`, `17`
  * **Output:** `48 is the largest`

### Q17. Smallest of Three Numbers
Input three numbers and find the smallest number.

### Q18. Leap Year
Write a program to determine whether a year is a leap year.
* **Hint:** A year is a leap year if it is divisible by 400 **OR** divisible by 4 but not by 100.

### Q19. Divisibility Test
Input a number and determine whether it is:
* Divisible by both 3 and 5
* Divisible only by 3
* Divisible only by 5
* Divisible by neither

### Q20. Electricity Bill
Calculate the electricity bill according to the following progressive rules:

| Units | Rate |
| :--- | :--- |
| 0–100 | ₹5/unit |
| 101–200 | ₹7/unit |
| 201–300 | ₹10/unit |
| Above 300 | ₹15/unit |

---

## 5. Nested `if` & Complex Logic

### Q21. Login System
Create a simple login program.
* **Input:** `Username`, `Password`
* **Rules:**
  * Username must be `"admin"`.
  * If username is correct, check the password.
  * Password must be `"1234"`.
  * Display specific, appropriate messages for an incorrect username versus an incorrect password.

### Q22. ATM Withdrawal
Given an initial state of `balance = 10000`, input a withdrawal amount.
* **Rules:**
  * Amount must be greater than 0.
  * Amount must be a multiple of 100.
  * Amount must not exceed the current balance.
  * Otherwise, display appropriate validation error messages.

### Q23. College Admission
Input `percentage` and `entrance_exam_score`. Admission is allowed only if:
* Percentage ≥ 60 **AND** entrance score ≥ 50.
* Otherwise, display the specific reason why the admission was rejected.

### Q24. Shopping Discount
Input the total purchase amount and calculate the final amount after applying discounts:
* Amount ≥ ₹10,000 → 20% discount
* Amount ≥ ₹5,000 → 10% discount
* Amount ≥ ₹2,000 → 5% discount
* Below ₹2,000 → No discount

### Q25. Triangle Classification
Input three sides of a triangle (a, b, c).
1. First determine whether the sides can form a valid triangle. 
   * *Hint:* Must satisfy a + b > c, b + c > a, and a + c > b.
2. If valid, classify it as: `Equilateral`, `Isosceles`, or `Scalene`.

### Q26. Profit or Loss
Input `Cost Price` and `Selling Price`. Calculate and display whether it results in a Profit, Loss, or No profit/no loss. Include the calculated profit or loss percentages where applicable.

### Q27. BMI Category
Input `weight` (in kg) and `height` (in meters). Calculate BMI = weight / height² and classify:

| BMI | Category |
| :--- | :--- |
| < 18.5 | Underweight |
| 18.5–24.9 | Normal |
| 25–29.9 | Overweight |
| ≥ 30 | Obese |

### Q28. Calculator
Input two numbers and an operator (`+`, `-`, `*`, `/`). Perform the operation using `if-elif-else`. Explicitly handle and prevent division by zero errors.
* **Example:**
  * **Input:** `10`, `5`, `*`
  * **Output:** `50`

### Q29. Employee Bonus
Input `salary` and `years_of_service`. Calculate the bonus amount and final salary based on these rules:
* Service ≥ 10 years → 20% bonus
* Service ≥ 5 years → 10% bonus
* Service ≥ 2 years → 5% bonus
* Otherwise → No bonus

### Q30. ATM Menu
Create an ATM program that accepts an operation input choice:
* `1` → Check Balance
* `2` → Deposit
* `3` → Withdraw
* `4` → Exit
Use decision statements to execute the operation. Ensure a validation check handles sufficient balance for withdrawals.

### Q31. Electricity Bill with Surcharge
Calculate a tiered slab electricity bill (using rules from Q20), then apply a surcharge:
* If base bill > ₹5,000 → add 10% surcharge
* If base bill > ₹10,000 → add 15% surcharge
* **Display format:** `Units consumed`, `Base bill`, `Surcharge`, and `Final bill`.

### Q32. Student Result System
Input individual marks for four subjects: `Python`, `SQL`, `Mathematics`, and `Statistics`.
* **Rules:**
  * Minimum 40 marks required in **every** subject to `Pass`; otherwise `Fail`.
  * Calculate overall percentage and assign a grade based on the percentage if they pass.

### Q33. Income Tax Calculator
Input annual income and calculate tax liability using regional income tax slabs. The program must explicitly output: `Income`, `Tax`, and remaining `Net income`.

### Q34. Login with Account Status
Input `username`, `password`, and `account_status`.
* **Rules:**
  * Correct username → check password.
  * Correct password → check account status.
    * If status is `"active"` → Login successful.
    * If status is `"blocked"` → Account blocked.
  * Wrong credentials at any stage → Login failed.

### Q35. Number Property Checker
Input an integer and determine all of its matching attributes simultaneously:
* Positive / negative / zero
* Even / odd
* Divisible by 3 / divisible by 5 / divisible by both 3 and 5 / divisible by neither
