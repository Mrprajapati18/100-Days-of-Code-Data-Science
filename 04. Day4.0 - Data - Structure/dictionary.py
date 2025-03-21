student = {'name' : 'Durgesh', 'branch': 'CSE'}

print(student)
print(student['name'])
print(student['branch'])
# print(student['roll'])  # Error


st = {
  1: 'Durgesh',
  2: 'Sam',
  3: 'raju',
  4: 'Sumit',
  5: 'Aditya'
}

print("Original Dictionary : ", st)

st[2] = 'arjun'
print("modifid dictionary : ", st)

del st[3]
print("Modified dictionary : ", st)

st.pop(1) 
print("Modified dictionary : ", st)
 
keys = st.keys()
print("keys : ", keys)
print(type(keys)) 


values = st.values()
print("Values : ", values)
print(type(values))

items = st.items()
print("Items : ", items)
print(type(items))