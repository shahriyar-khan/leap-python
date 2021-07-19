import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


p1 = input("Player #1 name: ")
p2 = input("Player #2 name: ")

roll1 = roll_dice()
roll2 = roll_dice()

print(p1, "rolled", roll1)
print(p2, "rolled", roll2)