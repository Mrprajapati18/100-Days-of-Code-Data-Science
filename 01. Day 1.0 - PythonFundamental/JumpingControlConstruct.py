  # Continue Statement
  
for i in range(1, 6):    # 1,2,3,4,5
  if i == 3:            # Skip the number of 3
    continue
  print("Hello!:", i)
  
  
  # Break Statement
  
for i in range(1,10):
    if i == 7:     # After 4 not any number printing
      break
    print("Hello Durgesh:", i)
   
   
   # Pass Statement
   
for i in range(1, 12):
     if i == 2:    # Number of placeholer is skip(2)
       pass
     else:
       print(i)