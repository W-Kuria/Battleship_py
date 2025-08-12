# Task: Prompt Player to Choose a Character

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
    character = "Unknown"
