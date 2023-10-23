vehicle_number = [1, 2, 3]
speed_in_kmh = [80, 50, 130]
mass_in_kg = [1500, 1800, 2100]
drag_coefficient = [0.31, 0.29, 0.25]
cross_sectional_area_in_m2 = [1.97, 2.01, 1.89] 
rolling_resistance = [0.015, 0.013, 0.020]

air_density = [1.204, 1.206, 1.199] 

ENERGY_EFFICIENCY_THRESHOLD_WATTS = 1000

for i in vehicle_number:    
    print(f"Vehicle {i}:")
    print(f"speed: {speed_in_kmh[i-1]} km/h")
    print(f"mass: {mass_in_kg[i-1]} kg")
    print(f"drag_coefficient: {drag_coefficient[i-1]}")
    print(f"cross_sectional_area: {cross_sectional_area_in_m2[i-1]} m^2")
    print(f"rolling resistance: {rolling_resistance[i-1]} N")
    print(f"air density: {air_density[i-1]} bar\n")
    
    # calculations for power consumptions
    drag_force = 0.5 * drag_coefficient[i-1] * air_density[i-1] * cross_sectional_area_in_m2[i-1] * ((speed_in_kmh[i-1]/3.6) ** 2)
    rolling_force = rolling_resistance[i-1] * mass_in_kg[i-1] * 9.81
    total_force = drag_force + rolling_force
    power = total_force * (speed_in_kmh[i-1]/3.6)
    
    print(f"Power consumption: {power:.2f} W\n")
    
    if power > ENERGY_EFFICIENCY_THRESHOLD_WATTS:
        print(f"Vehicle {i} is not fuel efficient!\n\n")
    else:
        print(f"Vehicle {i} is fuel efficient!\n\n")

    
    