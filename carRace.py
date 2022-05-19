race_count = 0
race_limit = 1000000


while race_count < race_limit:
    terminal_input = input("=> ")

    if terminal_input == "help":
        print('Type "start" to start the race')
        print('Type "stop" to stop the race')
        print('Type "quit" to exit the race')
        print('')

    elif terminal_input == "start":
        print('The race has started')
        print('')

    elif terminal_input == "stop":
        print("The race stopped, and you came out 1st")
        print('')

    elif terminal_input == "quit":
        print("You exited the game")
        print("")
        break

    elif terminal_input != "stop" or "start" or "quit":
        print(f"hey, I don't understand what '{terminal_input}' means")
        print('')
