# with open("Day 51/myfile.txt", "w") as f:

#  print(type(f))

#  f.write("12345678910111213 ")

#  f.seek(9)

#  data = f.read(5)
#  print(data)

with open('Day 51/myfile.txt', 'r') as f:
  
  f.seek(8)

  print(f.tell())
  
  data = f.read(5)
  print(data)  



f = open('Day 51/myfile2.txt', 'w')
 
f.write("Hello World") 
f.truncate(5)  # Truncate the file to 5 bytes



