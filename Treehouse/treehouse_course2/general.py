def check_lottery_number(num):
    lottery_numbers = [77, 24, 8, 18, 5, 64]

    if num in lottery_numbers:
        print(f'{num} is a winning number!')
    else:
        print(f'Try again, {num} is not a winning number.')

check_lottery_number(3)