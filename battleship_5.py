import random

# Game setup
player_hp = 100
enemy_hp = 100
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