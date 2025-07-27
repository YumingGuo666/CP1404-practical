from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    fancy_taxi = SilverServiceTaxi("Hummer", 200, fanciness=2)

    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    print(fancy_taxi)
    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.01, f"Fare calculation error! Expected ~48.78, got {fare:.2f}"

    print("Test passed!")


if __name__ == "__main__":
    main()
