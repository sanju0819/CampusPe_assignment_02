# number guessing game
# computer picks random number 1-100
# user gets 7 chances
# shows hints and best score


import random

best_score = None   # to store minimum attempts used


while True:

    num = random.randint(1, 100)
    attempts = 7
    used = 0

    print("\n--- guessing game started ---")

    while attempts > 0:

        g = int(input("guess number (1-100): "))
        used += 1
        attempts -= 1

        if g == num:
            print("correct ")
            print("attempts used:", used)

            # updating best score
            if best_score is None or used < best_score:
                best_score = used
                print("new best score:", best_score)

            break

        elif g > num:
            print("too high")

        else:
            print("too low")

        # close hint 
        if abs(g - num) <= 5:
            print("very close")

        print("attempts left:", attempts)

    else:
        print("you lost")
        print("number was:", num)

    # play again option
    again = input("\nplay again? (y/n): ").lower()
    if again != "y":
        print("thanks for playing")
        break