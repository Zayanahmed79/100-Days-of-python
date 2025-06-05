# f = open("Day 50/myfile.txt", "w")
# f.write("23,34,57 ")
# f.write("45,23,67 ")
# f.write("12,34,56 ")

f = open("Day 50/myfile.txt", "r")

i = 0
while True:
    i = i + 1
    line = f.readline() 
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"Student {i} Math's Marks : {m1}")
    print(f"Student {i} SST Marks : {m2}")
    print(f"Student {i} Science Marks : {m3}")
    print (f"Student {i} Total Marks : {int(m1) + int(m2) + int(m3)}")
    print(f"Student {i} Average Marks : {(int(m1) + int(m2) + int(m3)) / 3}")
    print("=========================================")

    

f.close()




