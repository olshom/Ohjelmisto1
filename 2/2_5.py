talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
mass = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
print("The weight in modern units: ")
print(f"{int(mass // 1000)} kilograms and {mass % 1000:.2f} grams.")
