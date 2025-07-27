while True:
    try:
        user_input = int(input("Enter square length : "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")

for i in range(user_input):
    for j in range(user_input):
        print("*", end="")
    print()