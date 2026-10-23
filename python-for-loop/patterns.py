# Questions 61-70: Pattern programs
# 61. Print pattern:  
#     ```text
#     * 
#     ** 
#     *** 
#     **** 
#     ***** 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# 62. Print pattern:  
#     ```text
#     ***** 
#     **** 
#     *** 
#     ** 
#     * 
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()


# 63. Print pattern:  
#     ```text
#     1 
#     12 
#     123 
#     1234 
#     12345 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# 64. Print pattern:  
#     ```text
#     1 
#     22 
#     333 
#     4444 
#     55555 

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()


# 65. Print pattern:  
#     ```text
#     * 
#     ** 
#     *** 
#     **** 
#     ***** 
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


# 66. Print pattern:  
#     ```text
#     1 
#     21 
#     321 
#     4321 
#     54321 
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()


# 67. Print a multiplication table from 1 to 10 using nested loops. 
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()


# 68. Print pattern:  
#     ```text
#     1 2 3 4 5 
#     1 2 3 4 5 
#     1 2 3 4 5 
#     1 2 3 4 5 
#     1 2 3 4 5 
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()


# 69. Print a 5 × 5 square:  
#     ```text
#     ***** 
#     ***** 
#     ***** 
#     ***** 
#     ***** 
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
    print()

# 70. Print this pattern:  
#     * 
#     *** 
#     ***** 
#     ******* 
#     ********* 
for i in range(1,6):
    for j in range(2*i-1):
        print("*",end="")
    print()