from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    print("\nAdd new guitars:")
    guitars += get_new_guitars()

    guitars.sort()
    print("\nAll Guitars (sorted):")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from CSV file into a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            for line in in_file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars

def save_guitars(filename, guitars):
    """Save guitars to CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    """Display all guitars nicely."""
    for i, guitar in enumerate(guitars, 1):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_str}")

def get_new_guitars():
    """Ask user to input new guitars and return them as a list."""
    new_guitars = []
    name = input("Name: ")
    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter correct values.")
        name = input("Name: ")
    return new_guitars

main()
