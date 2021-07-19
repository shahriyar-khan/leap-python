import random

choices = ["scissors", "rock", "paper"]
cpu_choice = choices[random.randint(0, 2)] # can also use random.choice([list])

user_choice = input("Do you want rock, paper, or scissors?\n")
print()
print("The CPU chose: {}".format(cpu_choice))

if cpu_choice == user_choice:
    print("TIE")
elif user_choice == "rock" and cpu_choice == "scissors":
    print("YOU WIN")
elif user_choice == "paper" and cpu_choice == "rock":
    print("YOU WIN")
elif user_choice == "scissors" and cpu_choice == "paper":
    print("YOU WIN")
else:
    print("You loose... CPU Wins")