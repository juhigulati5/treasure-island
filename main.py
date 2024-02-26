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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a crossroads. Which way would you like to go, left or right?\n").lower()
if(direction == "left"):
  lake = input("Good job, you survived the crossroads. Now, you've arrived at a lake. There is a boat in the middle of the lake. What would you like to do? type 'swim' to swim across or 'wait' to wait for a boat.\n").lower()
  if(lake == "wait"):
    door = input("You've made it to the island unharmed. You come across a house with three doors: red, yellow, and blue. Which door do you enter? type 'red', 'yellow', or 'blue'.\n").lower()
    if(door == 'red'):
      print("Congratulations, you found the treasure!")
    elif(door == 'blue'):
      print("There were pirates behind the door! Game over.")
    elif(door == 'yellow'):
      print("You got attacked by rabid monkeys. Game over.")
    else:
      print("That was not a valid option. Game over.")
      
  else:
    print("Sorry, you got eaten by crocodiles. Game over.")
else:
  print("Sorry, you fell into a hole. Game over.")
