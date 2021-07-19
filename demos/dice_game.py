import random

def main():
    p1 = input("Player #1 name: ")
    p2 = input("Player #2 name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(p1, "rolled", roll1)
    print(p2, "rolled", roll2)

    if roll1 > roll2:
        print(p1, "Wins!")
    elif roll2 > roll1:
        print(p2, "Wins!")
    else:
        print("You tie!")

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


main()