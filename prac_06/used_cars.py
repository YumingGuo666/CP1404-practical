"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
ORIGINAL_FUEL=100
INCREASED_FUEL=20
DRIVING_MILEAGE=115

from prac_06.car import Car

def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in limo after adding: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km")
    print(limo)


main()