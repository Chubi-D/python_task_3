import random

play = True

playerName = input('Player Name: ')

print(f"Hi {playerName} let's play a guessing game")

while play:
    easy = random.randint(1,10)
    medium = random.randint(1,20)
    hard = random.randint(1,50)

    print("Enter the level you wish to play" "\nType 'e' for easy, 'm' for medium, 'h' for hard")

    level_selection = True
    while level_selection:
        level = input()
        if level == 'e':
            print("\nAwesome level EASY begins ")
            level_selection = not True
            break
        if level == 'm':
            print("\nAwesome level MEDIUM begins")
            level_selection = not True
            break
        if level == 'h':
            print("\n Awesome level HARD begins")
            level_selection = not True
            break
        else:
            print("Invalid level selection. Enter either 'e', 'm' or 'h' ")
            break

    if level == 'e':
            print("You have only 6\n guesses to guess a number between 1-10 ")
            guess_left = 6
            while guess_left != 0:
                try1 = int(input("Enter your guess: \n"))
                if try1 == easy:
                    print("You got it Right!!!!")
                    break
                else:

                    print("That was wrong!!!")
                guess_left -= 1
                print('You now have ' +str(guess_left)+ ' guesses left')

                if guess_left == 1:
                    print('just 1 guess to go')

                if guess_left == 0:
                    print('Game Over!!')


    if level == 'm':
        print("You've got only 4\n guesses to guess a number between 1-20")
        guess_left = 4
        while guess_left != 0:
            try1 = int(input("Enter your guess: \n"))
            if try1 == medium:
                print("You got it Right!!!")
                break
            else:
                print("That was wrong")
            guess_left -=1
            print("You've got " +str(guess_left)+ "guesses left")

            if guess_left == 1:
                print('Just 1 guess to go')

            if guess_left == 0:
                print('Game Over!!')

    if level == 'h':
        print("You only have 2\n guesses to guess a number between 1-50 ")
        guess_left = 2
        while guess_left != 0:
            try1 = int(input("Enter your Guess:  \n "))
            if try1 == hard:
                print("That is Right!!!")
                break
            else:
                print("That was wrong")
            guess_left -= 1
            print("You've got " +str(guess_left)+ " guesses left")

            if guess_left == 1:
                print("Just 1 guess to go")

            if guess_left == 0:
                print("Game Over")

    play_again = True
    while play_again:
        again = input("Would you like to play again? y(Yes)or n(No) ").lower()
        if again == 'no':
            print("Thanks for playing")
            play_again = not True
            play = not True
        elif again == 'yes':
            print("Let's play again then  ")
            play_again = not True
            play = True

        else:
            print("please enter yes or no.")
            input()
            play_again = not True
            play = not True




