import random
import tkinter as tk
from tkinter import messagebox

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




def show_message(title,message):
    root=tk.Tk()
    root.withdraw() 
    messagebox.showinfo(title, message)
    root.destroy()  


# Task: Prompt Player to Choose a Characters
# 1: Show the available characters
print("Choose your character:")
print("1) Wizard")
print("2) Elf")
print("3) Human")

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
    show_message("Warning!", f"Please select an existing player,you have chosen {choice}")

# 4: Confirm the selection
print(f"You have chosen: {character}")


# Game setup
wizard_hp = 100
elf_hp = 100
player_damage = random.randint(15, 25)
enemy_damage = random.randint(10, 20)

print("=== BATTLESHIP COMBAT ===")
print(f"Player HP: {player_hp}")
print(f"Enemy Ship HP: {enemy_hp}")

# Battle simulation
while True:
    # Player's turn
    enemy_hp = enemy_hp - player_damage
    print(f"You hit the enemy ship for {player_damage} damage!")
    
    # Check for enemy's defeat
    if enemy_hp <= 0:
        print("Enemy ship destroyed! You win the battle!")
        break
    
    # Enemy's turn
    player_hp = player_hp - enemy_damage
    print(f"Enemy ship fires back for {enemy_damage} damage!")
    
    # Check for player's defeat
    if player_hp <= 0:
        print("Your ship has been sunk! You lost the battle!")
        break
    
    print(f"Player HP: {player_hp} | Enemy HP: {enemy_hp}")
    print("-" * 30)