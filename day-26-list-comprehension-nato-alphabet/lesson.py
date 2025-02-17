# Before
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

#Using List Comprehension
new_list1 = [n+1 for n in numbers]
print(new_list1)

#Can also work with Strings
name = "Dustin"
new_list2 = [letter for letter in name]
print(new_list2)

#Challenge - create a list from a range where each item is double
new_list3 = [n*2 for n in range(1,5)]
print(new_list3)

#Can Add Conditional to your list comprehension 
names = ["Marty", "Doc", "Biff", "George"]
#Add only name 4 characters or less
new_list4 = [name for name in names if len(name) <= 4]
print(new_list4)

#Challenge - add names larger than 4 in all caps
new_list5 = [name.upper() for name in names if len(name) >= 4]
print(new_list5)