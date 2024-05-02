import random

def main():
    true_number, guess_count = init_new_game()
    while True:
        user_input = input()
        guess_count += 1
        return_value = handle_cases(user_input, true_number, guess_count)
        match return_value:
            case 0:
                true_number, guess_count = init_new_game()
            case -1:
                print("Bye!")
                break
            case other:
                print("Too small.") if return_value < true_number else print("Too large.")

def init_new_game() -> (int, int):
    true_number = random.randint(1, 20)
    count = 0
    print("New Game Start.\nPress 'x' to exit anytime, 's' to reveal secret number, and 'n' to start a new game.\nGuess a whole number between 1 and 20: ")
    return true_number, count

def handle_cases(user_input: str, true_number: int, guess_count: int) -> int:
    if user_input.isnumeric() and 0 < (guess := int(user_input)) < 20:
        if guess == true_number:
            print(f"You guessed right!\nTotal guess count: {guess_count}")
            return 0 if input("Play again? [Y/N]: ").lower().startswith('y') else -1
        else:
            return guess
    match user_input:
        case 'x':
            print("Quiting Game.")
            return 0 if input("Play again? [Y/N]: ").lower().startswith('y') else -1
        case 's':
            print(f"True number was {true_number}.")
            return 0 if input("Play again? [Y/N]: ").lower().startswith('y') else -1
        case 'n':
            print("Restarting with a new secret number.")
            return 0
        case other:
            raise ValueError("Please insert a number between 1 and 20 or a control sequence character.")

main()