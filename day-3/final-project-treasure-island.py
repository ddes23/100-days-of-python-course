print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("\tYour mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

user_direction =  input("You're at a cross road. Do you want to go left or right? Type 'left' or 'right'. ")
direction = user_direction.lower()

if direction == "left":
    print("\nThe road to left has taken you to a isolated, but vast lake.\n")
    print("You see a large temple in the center. You have to decide to look for raft or swim.\n ")
    travel = input("Do you want to find a raft or swim? type 'raft' or 'swim'. ")
    if travel == "raft":
        print("\nWisely, you found a raft and reached the temple.\n")
        print("You see 3 doors. One is Red. One is Blue. One is Green.\n")
        door = input("What doors do you open? ")
        lowerdoor = door.lower()
        if lowerdoor == "red":
            print("\n\t\tYou chose...... wisely! The treasure is yours!")
        elif lowerdoor == "blue":
            print("\nBehind the Blue Door is full of snakes. Why'd it have to be snakes?")
            print("\n\t\t You've been eaten by an anaconda. RIP")
        elif lowerdoor == "green":
            print("\nBehind the Green Door is a large trap! Full of spikes!")
            print("\n\t\tYou got impaled and crush. Super dead like Alread Molina in Raiders. RIP")
    elif travel == "swim":
        print("Seriously? Definitely pirhanas in there. You died")
else:
    print("The road to the right had a lot of quicksand. You died like a dummy. RIP.")