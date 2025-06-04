dic1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(dic1["name"])


dic3 = {
    "303" : "Zayan",
    "404" : "ali",
    "505" : "Ahmed"
}

print(dic3["404"])
dic3["404"] = "Ali"
print(dic3["404"])

dic3["606"] = "Hassan"
print(dic3["606"])

# print(dic3["707"]) # This will through an error if item not found
# print(dic3.get("707"))  # This will return "Not Found" since key "707" does not exist

print(dic3.keys())  # This will return a view object that displays a list of all the keys in the dictionary
print(dic3.values())  # This will return a view object that displays a list of all the values in the dictionary


for key in dic3.keys():
    print(key)  # This will print each key in the dictionary

for key, value in dic3.items():
    print(f"{key}: {value}")  # This will print each key-value pair in the dictionary



