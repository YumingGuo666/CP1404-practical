from prac_09.unreliable_car import UnreliableCar

def main():
    reliable_car = UnreliableCar("Reliable", 100, 90.0)
    unreliable_car = UnreliableCar("Unreliable", 100, 10.0)

    print("Testing Reliable Car (90% reliability)")
    successful_drives = 0
    total_driven = 0
    for _ in range(100):
        distance = reliable_car.drive(1)
        if distance > 0:
            successful_drives += 1
        total_driven += distance
    print(f"Successful drives: {successful_drives} / 100")
    print(f"Total distance driven: {total_driven}")

    print("\nTesting Unreliable Car (10% reliability)")
    successful_drives = 0
    total_driven = 0
    for _ in range(100):
        distance = unreliable_car.drive(1)
        if distance > 0:
            successful_drives += 1
        total_driven += distance
    print(f"Successful drives: {successful_drives} / 100")
    print(f"Total distance driven: {total_driven}")


if __name__ == "__main__":
    main()
