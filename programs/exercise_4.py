import json

# Funktion zur Berechnung des Energieverbrauchs
def calculate_power_consumption(vehicle_data, speed_in_kmh):
    ENERGY_EFFICIENCY_THRESHOLD_WATTS = 1000

    # Definiere die Variablen für die Fahrzeuge
    mass_in_kg = []
    drag_coefficient = []
    cross_sectional_area_in_m2 = []
    rolling_resistance = []
    air_density = []

    # Iteriere über die Fahrzeugdaten und fülle die Listen
    for i, vehicle in enumerate(vehicle_data):
        mass_in_kg.append(vehicle['mass'])
        drag_coefficient.append(vehicle['drag_coefficient'])
        cross_sectional_area_in_m2.append(vehicle['cross_sectional_area'])
        rolling_resistance.append(vehicle['rolling_resistance_coefficient'])

        # Berechnungen für den Energieverbrauch
        air_density_vehicle = vehicle.get('air_density', 1.204)  # Standardwert 1.204, falls nicht angegeben
        air_density.append(air_density_vehicle)

        # Überprüfe, ob der Schlüssel 'vehicle_type' vorhanden ist, andernfalls verwende einen Standardwert
        vehicle_type = vehicle.get('vehicle_type', 'Unknown Vehicle Type')

        drag_force = 0.5 * drag_coefficient[i] * air_density[i] * cross_sectional_area_in_m2[i] * ((speed_in_kmh[i] / 3.6) ** 2)
        rolling_force = rolling_resistance[i] * mass_in_kg[i] * 9.81
        total_force = drag_force + rolling_force
        power = total_force * (speed_in_kmh[i] / 3.6)

        print(f"Vehicle {i + 1}:")
        print(f"vehicle_type: {vehicle_type}")
        print(f"mass: {mass_in_kg[i]} kg")
        print(f"drag_coefficient: {drag_coefficient[i]}")
        print(f"cross_sectional_area: {cross_sectional_area_in_m2[i]} m^2")
        print(f"rolling resistance: {rolling_resistance[i]} N\n")
        print(f"Power consumption: {power:.2f} W\n")

        if power > ENERGY_EFFICIENCY_THRESHOLD_WATTS:
            print(f"Vehicle {i + 1} is not fuel efficient!\n\n")
        else:
            print(f"Vehicle {i + 1} is fuel efficient!\n\n")

# Laden der Daten aus vehicles.json
try:
    with open('vehicles.json', 'r') as file:
        vehicles_data = json.load(file)
except FileNotFoundError:
    print("Fehler: Die Datei 'vehicles.json' wurde nicht gefunden.")
    exit()
except json.JSONDecodeError:
    print("Fehler: Fehler beim Decodieren der JSON-Datei 'vehicles.json'.")
    exit()

# Laden der Daten aus more_vehicles.json
try:
    with open('more_vehicles.json', 'r') as file:
        more_vehicles_data = json.load(file)
except FileNotFoundError:
    print("Fehler: Die Datei 'more_vehicles.json' wurde nicht gefunden.")
    exit()
except json.JSONDecodeError:
    print("Fehler: Fehler beim Decodieren der JSON-Datei 'more_vehicles.json'.")
    exit()

# Geschwindigkeiten für die Fahrzeuge aus beiden Dateien
speed_in_kmh_vehicles = [80, 50, 130]
speed_in_kmh_more_vehicles = [90, 60, 140]

# Berechne den Energieverbrauch für die Fahrzeuge aus der ersten Datei
calculate_power_consumption(vehicles_data, speed_in_kmh_vehicles)

# Berechne den Energieverbrauch für die Fahrzeuge aus der zweiten Datei
calculate_power_consumption(more_vehicles_data, speed_in_kmh_more_vehicles)
