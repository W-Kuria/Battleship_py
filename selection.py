
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