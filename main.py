import sys

class CarFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.AllowedVehiclesList = self.load_AllowedVehiclesList()
  # readFile AllowedVehiclesList.txt
    def load_AllowedVehiclesList(self):
        try:
            with open(self.file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"No file found at {self.file_path}. Creating a new one with initial vehicles.")
            initial_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
            with open(self.file_path, 'w') as file:
                for vehicle in initial_vehicles:
                    file.write(vehicle + '\n')
            return initial_vehicles

    def save_AllowedVehiclesList(self):
        with open(self.file_path, 'w') as file:
            for vehicle in self.AllowedVehiclesList:
                file.write(vehicle + '\n')

    def print_AllowedVehiclesList(self):
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for vehicle in self.AllowedVehiclesList:
            print(vehicle)

    def search_vehicle(self, vehicle_name):
      # convertInput type lowercase
        vehicle_name = vehicle_name.lower()
        if vehicle_name in [v.lower() for v in self.AllowedVehiclesList]:
            print(f"{vehicle_name.capitalize()} is an authorized vehicle")
        else:
            print(f"{vehicle_name.capitalize()} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
# fileEdit Add Vehicle
    def add_vehicle(self, vehicle_name):
        vehicle_name = vehicle_name.strip()
        if vehicle_name not in self.AllowedVehiclesList:
            self.AllowedVehiclesList.append(vehicle_name)
            print(f'You have added "{vehicle_name}" as an authorized vehicle')
            self.save_AllowedVehiclesList()
        else:
            print(f'"{vehicle_name}" is already an authorized vehicle')
#fileEdit Delete Vehicle
    def delete_vehicle(self, vehicle_name):
        vehicle_name = vehicle_name.strip()
        if vehicle_name in self.AllowedVehiclesList:
            confirm = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no): ')
            if confirm.lower() == 'yes':
                self.AllowedVehiclesList.remove(vehicle_name)
                print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle')
                self.save_AllowedVehiclesList()
        else:
            print(f'"{vehicle_name}" is not found in the Authorized Vehicles List')
  # displayText Choice Menu
    def display_menu(self):
        print("********************************")
        print("AutoCountry Vehicle Finder v0.5")
        print("********************************")
        print("Please enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")

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
                vehicle_name = input("Please enter the full Vehicle name you would like to add: ")
                self.add_vehicle(vehicle_name)
            elif choice == '4':
                vehicle_name = input("Please enter the full Vehicle name you would like to remove: ")
                self.delete_vehicle(vehicle_name)
            elif choice == '5':
                print("Thank you for using the AutoCountry Vehicle Finder, goodbye!")
                self.save_AllowedVehiclesList()  # Save changes before exiting
                sys.exit()
            else:
                print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    file_path = "AllowedVehiclesList.txt"
    car_finder = CarFinder(file_path)
    car_finder.run()
