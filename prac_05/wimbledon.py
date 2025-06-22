import csv

FILENAME = "wimbledon.csv"
def main():
    champions, champion_countries = read_wimbledon_data(FILENAME)
    display_champion_win_counts(champions)
    display_champion_countries(champion_countries)
def read_wimbledon_data(filename):
    champions = {}
    champion_countries = set()

    with open(filename, mode="r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            champion = row[2]
            country = row[1]

            champions[champion] = champions.get(champion, 0) + 1
            champion_countries.add(country)

    return champions, champion_countries

def display_champion_win_counts(champions):
    print("Wimbledon Champions:")
    for name, count in sorted(champions.items()):
        print(f"{name} {count}")

def display_champion_countries(countries):
    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_string)

main()