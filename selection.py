import random
# import tkinter as tk
# from tkinter import messagebox

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp=70
elf_hp=100
human_hp=150

wizard_damage=150
elf_damage=100
human_damage=20

dragon_hp=300
dragon_damage=50





# Task: Prompt Player to Choose a Characters
# 1: Show the available characters
print("Choose your character:")
print ("====================================")
print("1) Wizard")
print (" ")

print("2) Elf")
print (" ")

print("3) Human")
print (" ")
print ("====================================")
print("You will fight against a dragon!")
print ("====================================")

# 2: Get the player's choice
choice = input("Enter the number of your choice: ")


# 3: Match the choice to the character
if choice == "1":
    character = "Wizard"
elif choice == "2":
    character = "Elf"
elif choice == "3":
    character = "Human"
else:
     quit()


# 4: Confirm the selection
print ("====================================")
print(f"You have chosen: ||{character}||")
print ("====================================")
print (" ")





# Battle simulation
while True:
    # Player's turn
    if character=="Wizard":        
            wizard_hp = wizard_hp - dragon_damage
            
            dragon_hp = dragon_hp - wizard_damage

            print(f"You hit the enemy,dragons! hp is {dragon_hp} ")
            print (" ")
            print ("====================================")
            print (" ")
            if dragon_hp <= 0:
                print("Enemy ship destroyed! You win the battle!")
                print (" ")
                print ("====================================")

                break           
            print(f"The enemy hit you,your hp is {wizard_hp}")
            print (" ")
            print ("====================================")
            print (" ")

            if wizard_hp <= 0:
                print ("====================================")
                print("You loose!")
                print ("====================================")
                print ("====================================")
                

                break

    elif character=="Human":
            human_hp = human_hp - dragon_damage

            dragon_hp = dragon_hp - human_damage
            
            print ("====================================")

            print(f"You hit the enemy,dragons! hp is {dragon_hp} ")
            if dragon_hp <= 0:
                print ("====================================")

                print("Enemy ship destroyed! You win the battle!")
                break    
            print ("====================================")

            print(f"The enemy hit you,your hp is {human_hp}")
            if human_hp <= 0:
                print("You loose!")
                break

    elif character=="Elf":
            elf_hp = elf_hp - dragon_damage

            dragon_hp = dragon_hp - elf_damage
            print ("====================================")

            print(f"You hit the enemy,dragons! hp is {dragon_hp} ")
            if dragon_hp <= 0:
                print ("====================================")

                print("Enemy ship destroyed! You win the battle!")
                break
            print ("====================================")

            print(f"The enemy hit you,your hp is {elf_hp}")
            if elf_hp <= 0:
                print("You loose!")
                break
           
            
            