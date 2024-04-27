import random
import time

userScore = 0
computerScore = 0 
userName = None
clear = lambda: print("\033c", end="", flush=True)

clear()
userName = input("Please enter your name: ")
print(f"Name inputted: {userName}\n\n"
      "Let's play Pig Dice!\n"
      "The rules are simple; press enter to roll a die! Your goal is to get to 30 points before the pig.\n"
      "However, if you roll a ONE, your score is reset!\n")

while computerScore < 30 and userScore < 30:
    print(input("Press enter to roll!"))
    clear()
    print("Rolling the dice...")
    time.sleep(1.5)
    userRoll = random.randint(1,6)
    computerRoll = random.randint(1,6)
    userScore += userRoll
    computerScore += computerRoll
    if userRoll == 1:
        print(f"{userName} ROLLED A ONE! SCORE HAS RESET!\n")
        userScore = 0
    if computerRoll == 1:
        print("THE COMPUTER ROLLED A ONE! SCORE HAS RESET!\n")
        computerScore = 0
    print(f"{userName} rolled a {userRoll}! Their score is now {userScore}!")
    print(f"The computer rolled a {computerRoll}! Their score is now {computerScore}!\n")
    
    time.sleep(1)
#remember to handle ties past the 29 point mark
    if userScore >= 30 and computerScore >= 30:
        if userScore > computerScore:
            print(f"{userName} has the highest score and wins!\n"
                  "Thanks for playing!")
        elif computerScore > userScore:
            print("The computer has the highest score and wins!\n"
                  "Thanks for playing!")
        else:
            print("It's a tie! That's too bad!\n"
                  "Thanks for playing!")
    elif userScore >= 30:
        print(f"{userName} made to 30 and wins!\n"
              "Thanks for playing!")
    elif computerScore >= 30:
        print("The computer made it to 30 and wins!\n"
              "Thanks for playing!")
    
    

