gender = input("Enter your biological gender: ")
if gender == "male":
    hem_value = int(input("Enter your hemoglobin value (g/l): "))
    if hem_value < 134:
        print("your hemoglobin value is low.")
    elif 133 < hem_value < 168:
        print("Hemoglobin is good enough.")
    elif hem_value > 167:
        print("Your hemoglobin is high.")

elif gender == "female":
    hem_value = int(input("Enter your hemoglobin value (g/l): "))
    if hem_value < 117:
        print("your hemoglobin value is low.")
    elif 116<hem_value < 156:
        print("Hemoglobin is good enough.")
    elif hem_value > 155:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender input.")