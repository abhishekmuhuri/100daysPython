import random

def check_win(curr_word : str, alphas_guessed : list) -> bool:
    return curr_word == "".join(alphas_guessed)

def main():
    words = ["happy","life"]
    curr_word = random.choice(words)
    alphas_guessed = ['_' for _ in range(len(curr_word))]
    lifes = 4
    alphas_seen = set()
    while lifes > 0:
        char : str = input(f"Enter character to guess for {"".join(alphas_guessed)} || Lifes remaining : {lifes}]\n").lower()
        found = False
        for index,orig_char in enumerate(curr_word):
            if orig_char == char and alphas_guessed[index] == '_':
                alphas_seen.add(char)
                found = True
                alphas_guessed[index] = orig_char
                if(check_win(curr_word,alphas_guessed)):
                    print(f"You have won. Correct word: {curr_word}")
                    return
                else:
                    break
        
        if not found:
            if char not in alphas_seen:
                lifes-=1
                continue
            else:
                print(f"You have already guessed the letter '{char}'")

            
                
    print(f"You ran out of lifes. Correct word : {curr_word}")


if __name__ == "__main__":
    main()