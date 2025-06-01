MENU= """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""
def main():
    print(MENU)
    choice = input(">>> ").upper()
    score=""
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score
def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
def show_stars(score):
    print("*" * int(score))
main()

