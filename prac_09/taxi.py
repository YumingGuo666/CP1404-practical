"""
CP1404/CP5632 Practical
Taxi class that extends Car
"""

from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """
        Initialise a Taxi instance, based on parent class Car.
        No need to set price_per_km per instance.
        """
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation with fare distance and price per km."""
        return (f"{super().__str__()}, "
                f"{self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Reset the fare distance to begin a new trip."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """
        Drive the car like the parent class but also track fare distance.
        Returns the actual distance driven.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

