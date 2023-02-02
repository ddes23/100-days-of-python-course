# Instructions

# You are going to write a program that will mark a spot with an X.

# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}"
#  to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 

# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
y = int(position[0])
x = int(position[1])

print(position)
print(y)
print(type(y))
print(type(x))

if x == 1:
    row1[y-1] = 'X '
elif x == 2:
    row2[y-1] = 'X '
elif x == 3:
    row3[y-1] = 'X '


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
