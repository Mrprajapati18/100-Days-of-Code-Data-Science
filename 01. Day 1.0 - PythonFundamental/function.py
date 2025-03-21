# Functions 

def greet():
  print("Hello world!")
  
greet()  # Follow the Indentation


def fun():
    print("Instruction 1")
    print("Instruction 2")
    print("Instruction 3")
    print("Instruction 4")
    
print("Testing") 
fun()    

# Types Of Functions


# 1. No Parameter - No return value

# defining the function
def add():     # colon mean start the function
  a = 20
  b = 10
  sum = a + b
  print("Sum = ",sum)
  
# Calling the function  
add()  

# 2. No Parameter - Return Value

def add():
  c = 30
  d = 20
  sum_1 = c + d
  return sum_1

res = add()
print("Sum = ",res)
  
# 3. Parameter -  return value

def add(e, f):
  sum_2 = e + f
  return sum_2

res = add(10, 5)
print("Sum_2 = ",res)

  
# 4. Parameter -  No return value

def add(g, h):
  sum_3 = g + h
  print("Sum_3 = ",sum_3)

add(10,20)

