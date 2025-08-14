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

# Task: Prompt Player to Choose a Character

# 1: Show the available characters
print("Choose your character:")
print("1) Wizard")
print("2) Elf")
print("3) Human")

# 2: Get the player's choice
char_choice = input("Enter the number of your choice: ")



char_choice = input("Enter the number of your choice: ")

# 3: Match the choice to the character
if char_choice == "1":
    character = "Wizard"
    my_hp = wizard_hp
    my_damage = wizard_damage
    
elif char_choice == "2":
    character = "Elf"
    my_hp = elf_hp
    my_damage = elf_damage
    
elif char_choice == "3":
    character = "Human"
    my_hp = human_hp
    my_damage = human_damage
    
else:
    character = "Unknown"

# 4: Confirm the selection
print(f"You have chosen: {character}")