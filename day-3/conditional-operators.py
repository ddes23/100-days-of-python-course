#Logical Operators - AND, OR, & NOT

#Premise: people ages 45-55 have midlife crises, so they get in for free. 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollarcoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickers are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Congrats! Midlife crisis tickets are free!")
    else:
        bill = 12
        print("Adult tickets are $12")  

    wants_photo = input("Do you want a photo for $3? Enter Y or N")
    if wants_photo == "Y":
        bill += 3
        print(f"Your total is ${bill}")
    else:
        print(f"ok, your loss. Your total is ${bill}, cheapskate")
else:
    print("Sorry, you must be taller to ride this ride")
