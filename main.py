import sys

class CarFinder:
    def __init__(self, allowed_vehicles):
        self.allowed_vehicles = allowed_vehicles

    def print_allowed_vehicles(self):
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in self.allowed_vehicles:
            print(vehicle)
# displayText Choice Menu
    def display_menu(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.1")
        print("********************************")
        print("Please enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. Exit")
# computeDecision 1 OR 2
    def run(self):
        while True:
            self.display_menu()
            choice = input()

            if choice == '1':
                self.print_allowed_vehicles()
            elif choice == '2':
                print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    car_finder = CarFinder(allowed_vehicles)
    car_finder.run()
