speed_in_kmh = 80
mass_in_kg = 1500
drag_coefficient = 0.31
cross_sectional_area_in_m2 = 1.97
rolling_resistance = 0.015

air_density = 1.204 # 20 degree Celsius

drag_force = 0.5 *drag_coefficient*air_density *cross_sectional_area_in_m2 * ((speed_in_kmh/3.6)**2)
print(f"Drag force: {drag_force:.2f} Newton")

rolling_force = rolling_resistance * mass_in_kg * 9.81
print(f"Rolling resistance force: {rolling_force:.2f} Newton")

total_force = drag_force + rolling_force
print(f"Total force: {total_force:.2f} Newton")

power = total_force * (speed_in_kmh/3.6)
print(f"Power: {power:.2f} Watt")