
HEADER = """
  _____                       ______ __         _  __              __           
 / ___/__ __ ___  ___  ___   /_  __// /  ___   / |/ /__ __ __ _   / /  ___  ____
/ (_ // // // -_)(_-< (_-<    / /  / _ \/ -_) /    // // //  ' \ / _ \/ -_)/ __/
\___/ \_,_/ \__//___//___/   /_/  /_//_/\__/ /_/|_/ \_,_//_/_/_//_.__/\__//_/   
                                                                                """


GUESSES = 10

ATTEMPTS = 10


def main():
    print(HEADER)
    global ATTEMPTS
    print("Welcome to the Number Guessing Game! \n\
I'm thinking of a number between 1 and 100.\n \
        ")
    diff_choice = input("Choose a difficulty. Type 'easy' or 'hard':").strip().lower()
    
    if diff_choice == "hard":
        ATTEMPTS = 5
    
    import random
    num = random.randrange(1,100)

    while ATTEMPTS > 0:
        guess_num = int(input(f"You have {ATTEMPTS} attempts. Make a guess: "))
        if guess_num == num:
            print("You got it! The answer was {}".format(guess_num))
            return
        elif guess_num < num:
            print(f"Too low. Guess Again.")
        else:
            print(f"Too high.")
        ATTEMPTS-=1
    
    print(f"You've run out of guesses. The number was {num}")

if __name__ == "__main__":
    main()