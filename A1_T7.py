print("Calculate fuel consumption.")
feed = input("Enter travel distance (kilometers): ")
Distance = int(feed)
feed = input("Enter fuel usage (liters):")
FuelUsage = int(feed)
Consumption = Distance / FuelUsage
print(f"Fuel consumption is {Consumption} l per 100 km.")