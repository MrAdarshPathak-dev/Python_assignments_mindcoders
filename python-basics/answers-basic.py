# 1. Create a variable age and store the integer value 25 in it. Print its value and data type.
age=25
print(age,type(age))

#============================================================================

# 2. Create two integer variables a = 15 and b = 4. Find their sum, difference, product, division, floor division, and remainder.
a = 15
b = 4
sum = a+b
difference = a - b
product = a*b
divison= a/b
floor_division=a//b
remainder=a%b
print(f'''Sum:{sum} \nDifference:{difference} \nProduct:{product} \nDivison:{divison} \nFloor Division:{floor_division} \nRemainder:{remainder}''')

#============================================================================

# 3. Create a float variable `price = 499.75`. Print its value and data type.
number=499.75
print(number,type(number))

#============================================================================

# 4. Convert the integer `25` into a float and print the result.
num = 25
print(float(num))
# output 25.0

#============================================================================

# 5. Convert the float `45.89` into an integer and print the result.
num_float = 45.89
print(int(num_float))

#============================================================================

# 6. Create a string `name = "Python Programming"`. Find the length of the string using `len()`.
name="Python Programming"
print(len(name))

#============================================================================

# 7.  For `text = "hello python"`, use string methods to convert it to uppercase, title case, and capitalized form.
text = "hello python"
print(f"capitalized:{text.capitalize()}")
print(f"TitleCased:{text.title()}")
print(f"UpperCase:{text.upper()}")

#============================================================================

# 8. Create `text = "  Data Science  "`. Remove the spaces from both sides using a string method.
text1="   Data      Science   "
print(text1.strip())

#============================================================================

# 9. Create `message = "I like Java"`. Replace "Java" with "Python".
message = "I like Java"
replaced_message = message.replace("Java","Python")
print(replaced_message)

#============================================================================

# 10. Create `text = "apple,banana,mango"`. Split the string using a comma as the separator.
fruits = "apple,banana,mango"
splited_fruits= fruits.split(",")
print(splited_fruits)

#============================================================================

# 11. Create `fruits = ["apple", "banana", "mango"]`. Add "orange" to the end using a list method.
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

#============================================================================

# 12. Using `fruits = ["apple", "banana", "mango"]`, insert "grapes" at index 1.

fruits = ["apple", "banana", "mango"]
fruits[1]="grapes"
print(fruits)


#============================================================================

# 13. Create `numbers = [10, 20, 30, 40, 50]`. Remove 30 using a list method, then remove the last element using another list method.

numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)

#============================================================================

# 14. Create `numbers = [40, 10, 30, 20, 50]`. Sort the list in ascending order and then reverse it.

numbers = [40, 10, 30, 20, 50]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#============================================================================

# 15. Create `colors = ["red", "blue", "green", "blue", "yellow"]`. Find how many times "blue" occurs and the index of "green".

colors= ["red", "blue", "green", "blue", "yellow"]
print(colors.count("blue"))
print(colors.index("green"))


#============================================================================

# 16.  Create `marks = (70, 80, 90, 80, 85)`. Find the number of times 80 occurs using a tuple method.
marks = (70, 80, 90, 80, 85)
print(marks.count(80))


#============================================================================

# 17. Using `marks = (70, 80, 90, 80, 85)`, find the index position of 90.
marks = (70, 80, 90, 80, 85)
print(marks.index(90))

#============================================================================

# 18. Create `subjects = {"Python", "SQL", "Excel"}`. Add "Power BI" and then remove "SQL".
subjects = {"Python", "SQL", "Excel"}
subjects.add("Power BI")
print(subjects)
subjects.discard("SQL")
print(subjects) 

#============================================================================

# 19. Create `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`. Find their union, intersection, and difference A − B using set methods.


A = {1, 2, 3, 4}
B = {3, 4, 5, 6} 
union=A|B #returns a new  set of all unique elements
print("union:",union)
intersection=A&B #returns a new set of all the common elements
print("intersection:",intersection)

difference = A-B #returns  elments present in the first set but not in second set
print("difference:",difference)

#20. Create `A = {10, 20, 30}` and `B = {20, 30, 40}`. Find their symmetric difference.
A = {10, 20, 30}
B = {20, 30, 40}
symmetric_difference = A^B #returns unique elements of both set
print(symmetric_difference)