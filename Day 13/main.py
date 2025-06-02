nm = "zayan"
#print(nm.capitalize())
#print(nm.lower())
#print(nm.upper())
#print(nm.replace( "zayan" , "Talha"))
print(nm.rstrip("n")) # removes only the last character (Right side)
print(nm.lstrip("z")) # removes only the first character (Left side)
print(nm.strip("y")) #  can removes both the first and last character
print(nm.find("y")) # returns the index of the first occurrence of "a" # but if "a" is not found it will return -1
print(nm.index("a")) # returns the index of the first occurrence of "a" but if "a" is not found it will raise an error



hd = "Welcome to the world of Python"
print((hd.center(50,"~"))) # centers the string within 50 characters, padding with "*"




print(nm.count("a")) # counts the occurrences of "a" in the string : 2
print(nm.isalpha()) # checks if all characters are alphabetic : True
print(nm.isalnum()) # checks if all characters are alphanumeric : True
print(nm.isdigit()) # checks if all characters are digits : False
print(nm.isupper()) # checks if all characters are uppercase : False
print(nm.islower()) # checks if all characters are lowercase : True
print(nm.startswith("z")) # checks if the string starts with "z" : True
print(nm.endswith("n")) # checks if the string ends with "n" : True
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))       # True - as it says "to" is found in the range 4 to 10
print(str1.startswith("Welcome", 0, 7)) # True - as it says "Welcome" is found in the range 0 to 7  
print(hd.center(100, "-")) # centers the string within 50 characters, padding with "~"
print(nm.isprintable()) # checks if all characters are printable : True
print(hd.swapcase()) # swaps the case of all characters in the string : wELCOME TO THE WORLD OF pYTHON
print(hd.title()) # converts the first character of each word to uppercase and the rest to lowercase : Welcome To The World Of Python
print(hd.split()) # splits the string into a list of words : ['Welcome', 'to', 'the', 'world', 'of', 'Python']