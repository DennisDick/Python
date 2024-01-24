import json

# Constants
ENERGY_EFFICIENCY_THRESHOLD_WATTS = 1000

# Function to calculate drag force
def calculate_drag_force(drag_coefficient, air_density, cross_sectional_area, speed):
    return 0.5 * drag_coefficient * air_density * cross_sectional_area * ((speed / 3.6) ** 2)

# Function to calculate rolling resistance force
def calculate_rolling_force(rolling_resistance, mass):
    return rolling_resistance * mass * 9.81

# Function to calculate total force
def calculate_total_force(drag_force, rolling_force):
    return drag_force + rolling_force

# Function to calculate power consumption
def calculate_power(total_force, speed):
    return total_force * (speed / 3.6)

# Main function to process vehicle data
def process_vehicle_data(vehicle_data, speed_in_kmh):
    for i, vehicle in enumerate(vehicle_data):
        # Calculate forces
        drag_force = calculate_drag_force(vehicle['drag_coefficient'], vehicle.get('air_density', 1.204),
                                          vehicle['cross_sectional_area'], speed_in_kmh[i])
        rolling_force = calculate_rolling_force(vehicle['rolling_resistance_coefficient'], vehicle['mass'])
        total_force = calculate_total_force(drag_force, rolling_force)
        power = calculate_power(total_force, speed_in_kmh[i])

        # Print vehicle information
        print(f"Vehicle {i + 1}:")
        print(f"vehicle_type: {vehicle.get('vehicle_type', 'Unknown Vehicle Type')}")
        print(f"mass: {vehicle['mass']} kg")
        print(f"drag_coefficient: {vehicle['drag_coefficient']}")
        print(f"cross_sectional_area: {vehicle['cross_sectional_area']} m^2")
        print(f"rolling resistance: {vehicle['rolling_resistance_coefficient']} N\n")
        print(f"Power consumption: {power:.2f} W\n")

        # Check fuel efficiency
        if power > ENERGY_EFFICIENCY_THRESHOLD_WATTS:
            print(f"Vehicle {i + 1} is not fuel-efficient!\n\n")
        else:
            print(f"Vehicle {i + 1} is fuel-efficient!\n\n")

# Function to load JSON data
def load_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit()
    except json.JSONDecodeError:
        print(f"Error: Failed to decode the JSON file '{file_path}'.")
        exit()

# Load vehicle data from JSON files
vehicles_data = load_json_data('vehicles.json')
more_vehicles_data = load_json_data('more_vehicles.json')

# Speeds for vehicles from both files
speed_in_kmh_vehicles = [80, 50, 130]
speed_in_kmh_more_vehicles = [90, 60, 140]

# Calculate power consumption for vehicles from the first file
process_vehicle_data(vehicles_data, speed_in_kmh_vehicles)

# Calculate power consumption for vehicles from the second file
process_vehicle_data(more_vehicles_data, speed_in_kmh_more_vehicles)
