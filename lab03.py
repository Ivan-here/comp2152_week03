import random

#Dice Options created using list() and range()
diceOptions = list(range(1,7))

#weapon list
weapons = ["Fist","Knife", "CLub", "Gun", "Bomb", "Nuclear Bomb"]

print("Available Weapons: ",', '.join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1 <= value <= 6:
            return value
        else:
            print("Invalid Input! Enter a number between 1 to 6")

combatStrength = getCombatStrength("Please enter a number between 1 to 6 for a Player")
mCombatStrength = getCombatStrength("Please enter a number between 1 to 6 for the Monster")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    MonsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[MonsterRoll - 1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + MonsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {MonsterRoll}")
    print(f"\n Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"Hero Total Strength: {heroTotal}, Monster total {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Hero Wins!")
    elif heroTotal < monsterTotal:
        print("Monster Wins!")
    else:
        print("It's a tie!")

