print('Guess a number from 1 to 100')
all_numbers = list(range(1, 101))

while len(all_numbers) != 1:

    left = all_numbers[:len(all_numbers)//2]
    right = all_numbers[len(all_numbers) // 2:]
    print(f'1: {left}\n2: {right}')
    choise = int(input('Chose the output where you number is (1 or 2): '))
    match choise:
        case 1:
            all_numbers = left
        case 2:
            all_numbers = right

print(f'Your number is: {all_numbers[0]}')
