NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
import random
def main():
    try:
        number_of_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

def format_quick_pick(pick):
    return " ".join(f"{number:2}" for number in pick)

main()