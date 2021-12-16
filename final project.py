"""This code is a wishing simulator that allows the user to get pokemon through wishing. Users can get more wishes by answering math questions correctly!"""

import random

print("Welcome to the pokemon wishing simulator! You have 3 wishes. You may choose to get more!")
#welcome statement

pokemon_list_rare: list[str] = ["A", "B", "C"]
#defined list of rare pokemon

pokemon_list_ultra_rare: list[str] = ["D", "E", "F"]
#defined list of ultra rare pokemon

pokemon_list_legendary: list[str] = ["G", "H", "I"]
#defined list of legendary pokemon

pokemon_list_all: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

user_pokemon_list: list[str] = []
#defined list of user's pulled pokemon

wish_count = 3

def main():
    #main function
    wish = input("Would you like to wish? Input 'y' for yes, and 'n' for no: ")

    while wish == 'y':
        
        pokemon_choice = random.choices(pokemon_list_all, weights=(70, 70, 70, 20, 20, 20, 10, 10, 10), k=1)
        print(pokemon_choice)
        
        if pokemon_choice in pokemon_list_rare: 
            print("You got RARE ", pokemon_choice)

        elif pokemon_choice in pokemon_list_ultra_rare:
            print("You got ULTRA RARE ", pokemon_choice)

        elif pokemon_choice in pokemon_list_legendary: 
            print("You got LEGENDARY ", pokemon_choice)
        
        user_pokemon_list += [pokemon_choice]
        wish_count -= 1
        #ISSUE: user_pokemon+list and wish_count not referenced before assignment. Figure out how to fix it.


        wish = input("Would you like to wish again? Input 'y' for yes, and 'n' for no: ")

    return(user_pokemon_list)