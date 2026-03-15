from models import FuelDispenser, CarWash

# Create different station assets
asset1 = FuelDispenser("Fuel Pump 1", 500, 1.5)
asset2 = FuelDispenser("Fuel Pump 2", 300, 1.5)
asset3 = CarWash("Car Wash A", 40, 5)

# Store them in a list
station_assets = [asset1, asset2, asset3]

total_revenue = 0

# Loop through assets
for asset in station_assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue

print("\nTotal Station Revenue:", total_revenue)