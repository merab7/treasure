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

def play():
    name = input("Hello adventurer, tell me your name: ")

    def play_again():
        again = input("Do you want to play again? Y for yes, N for no\n")
        if again.lower() in ["y", "n"]:
            if again == "y":
                return play()
            else:
                print(f"By {name}!👋👋👋👋")

        else:
            print("You have only two options: Y or N")
            return play_again()

    def game_opening():
        left_or_right = input(f"Hello {name}, you have to choose your path. For left press L and for right press R\n")
        if left_or_right.lower() in ["l", "r"]:
            if left_or_right.lower() == "r":
                print(f"You chose wrong {name}, unfortunately you are killed by gigantic spiders 🕷️🕷️🕷️🕸️🕸️ ")
                play_again()
            else:
                def swim_or_wait():
                    swim_wait = input(f"You chose the correct path {name}, and you are on the edge of a big mountain. "
                                      f"In front of you is a sea. You have to choose to swim or wait for the boat. "
                                      f"Please {name}, press W for wait or S for swim\n")

                    if swim_wait.lower() in ["s", "w"]:
                        if swim_wait.lower() == "s":
                            print(f"You chose wrong {name}, unfortunately you are killed by sharks 🦈🦈 ")
                            play_again()
                        else:
                            def choose_door():
                                doors = input(f"You chose the correct path {name}, and you are on the island of treasure. "
                                              f"In front of you are three doors. You have to choose one of them. "
                                              f"Please {name}, press 1 for the first, 2 for the second, and 3 for the third\n")

                                if doors in ["1", "2", "3"]:
                                    if doors == "3":
                                        print(f"Congratulations {name}! You chose correctly, the treasure is yours 🪙🪙🪙🪙🪙🪙 ")
                                        play_again()
                                    else:
                                        print(f"You chose wrong {name}, unfortunately you are killed by darkness ⚫⚫ ")
                                        play_again()

                                else:
                                    print("You only have 3 options (1, 2, or 3)")
                                    choose_door()

                            choose_door()

                    else:
                        print("You only have 2 options: S or W")
                        swim_or_wait()

                swim_or_wait()

        else:
            print("You only have 2 options: L or R")
            game_opening()

    game_opening()

play()
