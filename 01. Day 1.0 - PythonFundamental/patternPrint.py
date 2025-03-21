# RightTrangle 
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#    for j in range(1, (i + 1)):
#        print("*", end=" ")
#    print()
     
# Hollow Rectangle

#  * * * * *
#  *       *
#  *       *
#  * * * * *


# for i in range(1,5):
#     for j in range(1,6):
#       if i==1 or i==4 or j==1 or j==5:   
#         print("*", end=" ")
#       else:
#         print(" ", end=" ")  
#     print() 
    
# Practice 
# 10 
# 20 * 30
# 40 * 50 * 60
# 70 * 80 * 90 * 100    

# Right Trangle

for i  in range(1,6):
  # For spaces
  for j in range(1, 6-i):
    print("_", end= "")
  # Digit
  x = 1
  for k in range(1, (2*i)):
    print(x, end="")
    if k < i:
      x = x+1
    else:
      x = x -1
    print()