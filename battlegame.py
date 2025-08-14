import random
import tkinter as tk
from tkinter import messagebox


wizard = "Wizard"
elf = "Elf"
human = "Human"


elf_hp=100
human_hp=150
wizard_hp=70

wizard_damage=150
elf_damage=100
human_damage=20

dragon_hp=300
dragon_damage=50







def show_message(title,message):
    root=tk.Tk()
    root.withdraw() 
    messagebox.showinfo(title, message)
    root.destroy()  


# Task: Prompt Player to Choose a Characters
# 1: Show the available characters
while True:
    
    print ("============================")
    print("Choose your character:")
    print (" ")
    print("1) Wizard")
    print (" ")
    print("2) Elf")
    print (" ")
    print("3) Human")
    print ("============================")
# 2: Get the player's choice
    character_choice = input("Choose your character: ")
    print (" ")

# 3: Match the choice to the character

    character=""
    if character_choice == "1":
        character = "Wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character_choice == "2":
        character = "Elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character_choice == "3":        
        character = "Human"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    else:
        show_message("Warning!", f"Please select an existing player,you have chosen {choice}")
        quit()

# 4: Confirm the selection
    print(f"You have chosen: {character}")


# Game setup


    print("=== BATTLESHIP COMBAT ===")
    print(f"You are playing as {character} with {my_hp} HP and {my_damage} damage.")
    print(f"Dragon HP is: {dragon_hp}")
    print("_____________________________________________________________________________________________")
    print("LET THE GAMES BEGIN!")

while True:
    # Player attacks
    dragon_hp -= my_damage
    print(f"You hit the enemy dragon! Dragon's HP is now {dragon_hp}")
    print (" ")
    if dragon_hp <= 0:
        print("Enemy ship destroyed! You win the battle!")
        print (" ")
        break

    # Dragon attacks
    
    my_hp -= dragon_damage
    print(f"The dragon hits you! Your HP is now {my_hp}")
    print (" ")

    if my_hp <= 0:
        print("YOU LOSE!")
        break         