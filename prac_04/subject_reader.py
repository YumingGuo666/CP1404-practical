"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_list=[]
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_list.append(parts)
    input_file.close()
    return subject_list

def display_subject_details(data):
    for subject in data:
        code = subject[0]
        lecturer = subject[1]
        students = subject[2]
        print(f"{code} is taught by {lecturer} and has {students} students")


main()