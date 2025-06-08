name = input("Enter your name: ")
out_file = open("name.txt", "w")  # open file for writing
out_file.write(name)
out_file.close()
in_file = open("name.txt", "r")  # open file for reading
name = in_file.read().strip()    # strip to remove trailing newline
in_file.close()
print(f"Hi {name}!")
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
print(total)
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())  # strip newline, convert to int
print(total)
