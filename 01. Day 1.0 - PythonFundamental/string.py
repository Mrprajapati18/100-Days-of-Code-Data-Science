# Single Line String to use the i  inclose bracket inverted comma
Name = 'Durgesh Kr Prajapati'
Tech = 'Python 3.0'
print (Name)
print (Tech)
# Multiline String we use the 3 inverted comma
print("=================================================")
Address = ''' Kodnest
             BTM
             Bagaluru 
           '''
print (Address)    
# If incase of any name use apastraphe comma the 
            
S1 = " Let's Go to play"
print (S1)
print("=================================================")
# Store a variable and print it
S = "python is fun"
S[0:6]
S[7:9]
S[7:]
S[10:13]
S[:9]
print(S)

print("===================================================")
S2 = "python is fun"
# To find the length of String
print(len(S2))

# To convert the all string in Upper case
print(S2.upper())

# To find the character present in the string or not
print(S2.find("fun"))

# TO replace the Python to Java
print(S2.replace("python","Java"))

print("================================================")

tech = "python,java,golong"
technology = tech.split(",")
print(technology)

join_text = " - ".join(technology)
print(join_text)

print("=====================================================")
# Concatinate method(using + operater)
p1 = "Hello"
p2 = p1 + (" World!")
print(p1)
print(p2)

# For same string (is , id)
print("======================================================")
p3 = "Python"
p4 = "Python"
print(p3 is p4)

# using id operator
print(id(p3))
print(id(p4))

print("================================================")
# using Slice 
message = 'Python is an amazing language!'
part1 = message[0:6]
part2 = message[13:]
part3 = message[7:9]

print("Part 1: " + part1)
print("Part 2: " + part2)
print("Part 3: " + part3)

print("============================================")
# Using slice for negative index
message1 = 'Python is an amazing language!'
part4 = message[-30:-24]
part5 = message[-17:]
part6 = message[-23:-21]

print("Part 4: " + part4)
print("Part 5: " + part5)
print("Part 6: " + part6)
