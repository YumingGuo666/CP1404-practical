"""Project Management Application."""

from project import Project
import datetime

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "q":
        print_menu()
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            if input(f"Would you like to save to {FILENAME}? ").lower() in ["y", "yes"]:
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


def print_menu():
    print("- (L)oad projects  \n- (S)ave projects  \n- (D)isplay projects  \n- (F)ilter projects by date")
    print("- (A)dd new project  \n- (U)pdate project\n- (Q)uit")

def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as in_file:
            next(in_file)  # skip header
            for line in in_file:
                name, date, priority, cost, percent = line.strip().split('\t')
                projects.append(Project(name, date, priority, cost, percent))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return projects

def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(project.to_tab_string(), file=out_file)

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")

def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
        filtered = [p for p in projects if p.start_after(filter_date)]
        for p in sorted(filtered, key=lambda p: p.start_date):
            print(p)
    except ValueError:
        print("Invalid date format")

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))
    try:
        new_project = Project(name, start_date_str, priority, cost, percent)
        projects.append(new_project)
    except ValueError as e:
        print(f"Invalid input: {e}")

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)

        new_percent = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_percent:
            project.completion_percentage = int(new_percent)
        if new_priority:
            project.priority = int(new_priority)
    except (ValueError, IndexError):
        print("Invalid selection or input.")

main()
