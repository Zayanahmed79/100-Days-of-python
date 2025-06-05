# f = open("Day 49/text.md", "r")
# # Read the contents of the file
# contents = f.read()
# print(contents)  # Output: the contents of text.mdj
# f.close()



# f = open('Day 49/myfile.txt', 'w')
# f.write('Shafique Here!')


with open('Day 49/myfile.txt', 'w') as f:
    f.write('Shafique Here!')
    f.write('\nThis is a new line.')
    f.write('\nAppending another line.')



