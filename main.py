import random

Numbgames = input("How many games you want to play?  ")
while not Numbgames.isdigit():
    print('Chose number! '),
    Numbgames = input()
else: print("You want to play " +Numbgames +" games.")
for i in range(int(Numbgames)):

    hand_signals = ["Rock", "Papper", "Scissors"]
    opponent = random.choice(hand_signals)

    your_hand = input(hand_signals)
    while hand_signals.__contains__(your_hand) != True:
        print("Error")
        your_hand = input(hand_signals)
    else:
        print("Ok")

    print("Computer chose: " +opponent +"   \n"
    "You chose: " +your_hand +
          " \n"

    )

    print("Result:")

    if opponent == "Rock" and your_hand == "Papper":
        print("You win! :)"),
    elif opponent == "Rock" and your_hand == "Scissors":
        print("You lose! :("),
    elif opponent == "Papper" and your_hand == "Rock":
        print("You lose! :("),
    elif opponent == "Papper" and your_hand == "Scissors":
        print("You win! :)"),
    elif opponent == "Scissors" and your_hand == "Rock":
        print("You win! :)"),
    elif opponent == "Scissors" and your_hand == "Papper":
        print("You lose! :("),
    else: print("Draw :|")
