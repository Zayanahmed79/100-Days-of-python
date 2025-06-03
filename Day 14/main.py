# Age = int(input("Enter your age:"))


#conditional operators : 
# ==, !=, >, <, >=, <=


# if(Age < 18):
#     print("You are not eligible to vote")
# else:
#     print("You are eligible to vote")
#     print("You can vote for the following parties:")
#     print("1. PTI")
#     print("2. PML-N")
    # print("3. PPP")
    # print("4. JUI-F")
    # print("5. ANP")
    # print("6. MQM")
    # print("7. BAP")
    # print("8. BNP")
    # print("9. JI")
    # print("10. TLP")


# elif 

num = int(input("Enter a number: "))

print("!! Example of Elif-Else !!")
if (num < 0 ):
    print("less then xero")
elif(num  == 0 ):
    print("number is zero")
elif(num == 10000):
    print("Number is 10k")
else:
    print("Greater then xero")


# nested if-else

print("!! Example of Nested If-Else !!")

if (num < 0):
    print("less then xero")
else:
    if (num == 0):
        print("number is zero")
    else:
        if (num == 10000):
            print("Number is 10k")
        else:
            print("Greater then xero")