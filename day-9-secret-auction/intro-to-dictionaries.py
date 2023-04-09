programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

#Dictionaries use curly braces {} rather than [] like a list. Syntax with key:value is critical

#Adding things to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

#Can creat empty dictionaries and at later stage add to it
empty_dic = {}

#Wipe and existing dictionary
# programming_dictionary = {}

print(programming_dictionary)

#edit an item in a dictionary

programming_dictionary["Bug"] = "an insect"
print(f"\n{programming_dictionary}")

#Loop through dictionary - for loop is printing just keys
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])