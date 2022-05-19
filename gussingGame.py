secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number from 1 to 9 > "))

    if guess == secret_number:
        print("🎉🎉🎉 You guessed the correct number")
        break
    else:
        print("😞😞 You guessed the wrong number")
