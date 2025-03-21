
# Simple If

print("Welcome to college")
marks = int (input("Enter marks: "))

if marks > 80:
   print("Welcome to Tech Club")
   
   # Simple if else
   
   num = int(input("Enter a number: "))
   
if num%2 == 0:
     print("Even Number")
else:
     print("Odd Number")  
     
     
# else if else (elif)

'''
90 - 100 -> "Laptop"
76 - 85  ->  "Tablet"
60 - 75  ->  "Smart Watch"
40 - 50  -> "Bycycle"
bellow 40 -> "get lost"
'''

marks_1 = int(input("Enter the number: "))

if marks_1 >= 91:
   print("Laptop")
   
elif marks_1 >= 77:
  print("Tablet")  
  
elif marks_1 >= 65:
  print("Smart watch")
  
elif marks_1 >= 45:
  print("Bycycle")
  
else:
  print("Try Again")     
  
  
  # Practice Question
  '''
  5000 -> 20%
  3500 - 4999 -> 15%
  1500 - 3500 -> 10%
  else - no discount
  
  -------------------
  input : 8000
  output: 
  
  discount eligible: 20%
  final amount: 6400
  ''' 
  
  