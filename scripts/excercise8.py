#!/usr/bin/env python3.7

rock = "R"
paper = "P"
scissors = "S"

possibleAnswers = [rock, paper, scissors]

winnerMap = {rock: scissors, paper: rock, scissors: paper}

def startGame():
    go = True

    while(go):
        user_1_input = input("First user choice: Rock[R], Paper[P], Scissors[S]? ")
        if user_1_input not in possibleAnswers:
            print("Unknown sign!")
        else:
            user_2_input = input("Second user choice: Rock[R], Paper[P], Scissors[S]? ")
            if user_2_input not in possibleAnswers:
                print("Unknown sign!")
            else:
                getWinner(user_1_input, user_2_input)

        end = input("Do you want to continue? [Y/N]: ")
        if end == "N":
            go = False
    print("Game finished!")
            
def getWinner(answer1, answer2):
    if answer1 == answer2:
        print("It's a draw!")
    else:
        if winnerMap[answer1] == answer2:
            print("First user won!")
        else:
            print("Second user won!")


startGame()
