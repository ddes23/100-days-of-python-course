# #Function Review

# # Plain function to reduce code 

# # def my_function():
# #     #Do this
# #     #then do this
# #     #Finally do this

# # #Function with Inputs

# # def my_function(something):
# #     Do this with something
# #     The do this
# #     Finally do this

# # Function with Outputs - using the keyword of "return" for the output
# def my_fuction():
#     result = 3 * 2
#     return result

def format_name(f_name, l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"

formatted_string = format_name("dUstiN", "dESPRES")
print(formatted_string)
