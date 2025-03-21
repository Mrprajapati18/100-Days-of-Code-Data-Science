# 1.for Loop

# for i in range(4):
#   print("Hello World!")
  
# for i in range(4):  # range function is always start (0 , 4) 0 incusive but 4 is not inculsive
#     print(i)
    
# for j in range(9):
#   print(j) 

# print the table of 10   
'''
10 X 1 = 10
10 X 2 = 20
10 X 3 = 30
10 X 4 = 40
...........
10 X 10 = 100

'''
# num = int(input())
# for i in range(1, 11):
#   print(num,"X",i,"=",(i * num))
  
# 2. While Loop

'''
number ? 5
square = 25
Continue ? yes

number ? 3
square = 9
continue ? yes

number ? 10
square = 100
continue ? no

''' 

# attempt = True
# while attempt == True:
#   num = int (input("please enter the number"))
#   sq = num * num
#   print("Squre = ", sq)
#   attempt = bool(input("press enter to exit or another key to continue - "))

# attempt = "Yes"
# while attempt == "Yes":
#   num = int(input("please enter the number"))
#   sq = num * num
#   print("Squre = ", sq)
#   attempt = input("Continue? Enter yes or no - ")
  
# number is palindrome or not

# num_1 = int(input("Please enter a number"))
# num_copy = num_1
# rev = 0
# while num_1 != 0:
#   dig = num_1 % 10
#   rev = rev * 10 + dig
#   num_1 = num_1 // 10
  
# if num_copy == rev:
#   print("Palindrome")
# else:
#   print("not palindrome")  
  
# table of the number using while loop

# num_2 = int(input("Enter the tale of the number"))




# print the squre of the pattern print

'''
*****
*****
*****
*****
'''
rows = 4
cols = 5

for i in range(rows):
    print("*" * 5)

