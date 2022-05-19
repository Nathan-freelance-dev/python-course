car_is_started = False
has_car_stopped = False

while True:
    terminal_input = input("=> ").lower()

    if terminal_input == "help":
        print('Type "start" to start the race')
        print('Type "stop" to stop the race')
        print('Type "quit" to exit the race')
        print('')

    elif terminal_input == "start":
        if car_is_started:
            print("The car has already started")
        else:
            car_is_started = True
            print('The race has started')
        print('')

    elif terminal_input == "stop":
        if has_car_stopped:
            print("The car has ready been stopped")

        else:
            has_car_stopped = True
            print("The car has stopped, and the race was ended")

        print('')

    elif terminal_input == "quit":
        print("You exited the game")
        print("")
        break

    elif terminal_input != "stop" or "start" or "quit" or "help":
        print(f"hey, I don't understand what '{terminal_input}' means")
        print('')
