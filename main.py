import sys

class CarFinder:
    def __init__(self, AllowedVehiclesList):
        self.AllowedVehiclesList = AllowedVehiclesList

    def print_AllowedVehiclesList(self):
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in self.AllowedVehiclesList:
            print(vehicle)

    def search_vehicle(self, vehicle_name):
        vehicle_name = vehicle_name.lower()  # convertInput type lowercase
        if vehicle_name in [v.lower() for v in self.AllowedVehiclesList]:
            print(f"{vehicle_name.capitalize()} is an authorized vehicle")
        else:
            print(f"{vehicle_name.capitalize()} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
# displayText Choice Menu
    def display_menu(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.2")
        print("********************************")
        print("Please enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. Exit")
# computeDecision 1 OR 2 OR 3
    def run(self):
        while True:
            self.display_menu()
            choice = input()

            if choice == '1':
                self.print_AllowedVehiclesList()
            elif choice == '2':
                vehicle_name = input("Please enter the full Vehicle name: ")
                self.search_vehicle(vehicle_name)
            elif choice == '3':
                print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    car_finder = CarFinder(AllowedVehiclesList)
    car_finder.run()
