import random

def ask_rounds():
    while True:
        user_input = input("How many rounds would you like to play? Choose between 1 and 40: ")
        try:
            rounds = int(user_input)
            if 1 <= rounds <= 40:
                return rounds
            else:
                print("Please enter a number between 1 and 40.")
        except ValueError:
            print("Please enter a valid integer between 1 and 40.")

def play_round(round_number):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    correct_answer = a * b

    while True:
        user_input = input("Round " + str(round_number) + ": What is the result of " + str(a) + " * " + str(b) + "? ")
        try:
            user_answer = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer answer.")

    if user_answer == correct_answer:
        print("That is correct!")
        return 1
    else:
        print("That is incorrect. The correct answer is " + str(correct_answer) + ".")
        return 0

def main():
    print("Welcome to the multiplication quiz (1-20)!")
    rounds_to_play = ask_rounds()
    score = 0

    for round_number in range(1, rounds_to_play + 1):
        score += play_round(round_number)

    print("")
    print("You answered " + str(score) + " correct out of " + str(rounds_to_play) + ".")

if __name__ == "__main__":
    main()