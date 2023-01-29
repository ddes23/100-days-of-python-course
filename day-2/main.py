#Data Types

# Strings

# Have to create with double quotes. 
# Because they are strung together, can grab individial characters - call subscripting.
# between square brackets [] begins at position 0. 
# Numbers in double quotes will be interpreted as strings

print("Hello"[4])

print("123" + "456")

#Integer
# Whole numbers, no decimal. Just need to write number, no quotes

print (123 + 456)

# type() function
# Help tell you what type of data you have

num_char = len(input ("What is your name?")) 
type(num_char) #output here is <class 'int'>

num_char = len(input ("What is your name?")) 
new_num_char = str(num_char) #str() function converts object to string

