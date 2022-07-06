import random


def monty_hall(plays, switch):
    doors = [False, False, False]

    wins = 0
    for i in range(plays):
        car_location = random.randint(0, 2)
        initial_choice = random.randint(0, 2)
        final_choice = initial_choice

        doors[car_location] = True

        reveal_location = 0
        possible_reveal_locations = []
        for i in range(len(doors)):
            if i != initial_choice and i != car_location:
                possible_reveal_locations.append(i)

        reveal_location = possible_reveal_locations[random.randint(0, len(possible_reveal_locations) - 1)]

        if (switch):
            for i in range(len(doors)):
                if i != initial_choice and i != reveal_location:
                    final_choice = i

        result = "Initial choice: {0} | Car location: {1} | Reveal location: {2} | Final choice: {3}".format(initial_choice + 1, car_location + 1, reveal_location + 1, final_choice + 1)
        if final_choice == car_location:
            print(result + " - WIN")
            wins += 1
        else:
            print(result + " - LOSE")

    print("Win rate: {0:.2f}%".format((wins/plays) * 100))

if __name__ == '__main__':
    monty_hall(10000, True)

