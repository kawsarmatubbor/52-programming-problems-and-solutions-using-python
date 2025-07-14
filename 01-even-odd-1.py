while True:
    try:
        user_input = int(input("Enter a number : "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")

if user_input % 2 == 0:
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")
