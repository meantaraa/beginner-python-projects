print(r'''
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

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Function for input validation
def get_valid_input(prompt, valid_choices):
    choice = input(prompt).lower()
    while choice not in valid_choices:
        print(f"Invalid choice. Please choose one of the following: {', '.join(valid_choices)}")
        choice = input(prompt).lower()
    return choice

# first choice
fork = get_valid_input("You're hiking on a wooded trail and come to a fork in the road. Do you go 'left' or 'right'? \n", ["left", "right"])

if fork == "left":
    lake = get_valid_input("You reach the shore of a large lake with an island in the center.\n  Do you wait for the ferryman or just swim across? (Choose 'wait' or 'swim') \n", ["wait", "swim"])

    # second choice
    if lake == "wait":
        cave = get_valid_input("The ferryman gladly takes you across the lake and you walk into the jungle.\n After a short while you come upon a large cave.\n Curiously you enter.  Oddly enough, inside the cave are three doors: A Red, Blue, and Yellow door.  Which do you choose, 'red', 'blue', or 'yellow'? \n", ["red", "blue", "yellow"])

        # final choice
        if cave == "red":
            print("As the door closes and locks behind you, a giant scorpion surprises you...\n it stings and eats you. Game Over.")
        elif cave == "blue":
            print("As the door opens, a giant troll grabs you by the neck...he kills and eats you.  Game Over.")
        elif cave == "yellow":
            print("The door slowly swings open to reveal...The lost treasure of Jack Sparrow!!!  Congratulations Mate, You WIN!")
        else:
            print("You turn to leave and are suddenly attacked by a large mountain lion...and Die.  Game Over.")
    else:
        print("After a few minutes in the water, you are pulled under and drown by a large crocodile.  Game Over.")
else:
    print("About 50 yards in, you are attacked & mauled to death by a giant momma grizzly bear.  Game Over.")
