import os

# for i in range(92 , 100):
#     os.rename(f"Day{i+1}", f"Day {i+1}" )
# This code renames directories from "Day92" to "Day 93", "Day94", ..., "Day 100"

# os.mkdir("Day 100") 


# folders = os.listdir("/IT work/100 days of python/100-Days-of-python")
# print(folders)



# for folder in folders:
#     print(os.listdir(f"/IT work/100 days of python/100-Days-of-python=/{folder}"))

print(os.getcwd())


import os

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()
