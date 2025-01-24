fish_size = int(input("Enter the fish length: "))
if fish_size < 42:
    print("You have to release the fish back.")
    print(f"Your fish has to be longer on {42-fish_size} cm.")
else:
    print("You can caught this fish.")