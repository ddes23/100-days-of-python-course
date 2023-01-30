# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()
tcount = ((lower_name1.count("t")) + (lower_name2.count("t")))
rcount = ((lower_name1.count("r")) + (lower_name2.count("r")))
ucount = ((lower_name1.count("u")) + (lower_name2.count("u")))
ecount = ((lower_name1.count("e")) + (lower_name2.count("e")))
lcount = ((lower_name1.count("l")) + (lower_name2.count("l")))
ocount = ((lower_name1.count("o")) + (lower_name2.count("o")))
vcount = ((lower_name1.count("v")) + (lower_name2.count("v")))
num1 = tcount + rcount + ucount + ecount
num2 = lcount + ocount + vcount + ecount
score = str(num1) + str(num2)
intscore = int(score)

if intscore < 10 or intscore > 90:
    print(f"Your score is {intscore}, you go together like coke and mentos.")
elif intscore >= 40 and intscore <= 50:
    print(f"Your score is {intscore}, you are alright together.")
else:
    print(f"Your score is {intscore}.")
