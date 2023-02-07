# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Jobba")
#     print("The")
#     print("Hutt")

# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do, {name}?")

# # greet_with_name("Dustin")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How's the weather in {location}?")

# name = input("What is your name?")
# greet_with(name, "Philly")

#Challenge - define function with keyword arguments, rather than positional
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's the weather in {location}?")


greet_with(location="Philly", name="Dustin")
