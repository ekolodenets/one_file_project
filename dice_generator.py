from files.dice_draw import dice_sides
import random
EXIT_COMMANDS = ['stop', 'exit']


def roll_dice(times):
    results = []
    [results.append(random.randint(1, 6)) for _ in range(times)]
    return results


def draw(lst):
    list_sides = []
    for i in lst:
        list_sides.append(dice_sides[i])
        moved_sides = list(zip(*list_sides))
        for j in moved_sides:
            print(*j)


def main():
    while True:
        command = input('How many dice you want to roll? ')
        if command in EXIT_COMMANDS:
            break
        else:
            try:
                command = int(command)
                draw(roll_dice(command))
            except ValueError:
                print('Invalid input')


if __name__ == '__main__':
    main()
