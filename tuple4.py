# The treasure hunt begins!
team = ("Adithi", "Daneen", "Jawad")  # The tuple holds the names of the team members
print("Team members:", team)

# Tuples ensure no changes to the team during the treasure hunt.
print("\nOops! Someone tries to change the team:")
try:
    team[0] = "Adithi"  # Attempt to modify the tuple
except TypeError as e:
    print("Error:", e)

print("\nThe team stays the same:", team)

# Packing and unpacking their adventure details
adventure = ("Secret Cave", 3, "Golden Treasure")
location, days, treasure = adventure
print("\nAdventure details:")
print("Location:", location)
print("Days to explore:", days)
print("Treasure:", treasure)

# Returning from the journey with results
def find_treasure():
    return "Golden Treasure", 500  # Treasure name and value in coins

result = find_treasure()
print("\nThe team found a:", result[0])
print("Worth:", result[1], "coins")

# A map using coordinates as keys for treasure locations
map = {(0, 0): "Entrance", (1, 2): "Mystic Lake", (3, 4): "Treasure Room"}
print("\nMap coordinates:")
for coords, location in map.items():
    print(f"Coordinates {coords}: {location}")
