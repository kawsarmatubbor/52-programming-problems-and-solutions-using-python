while True:
    try:
        user_input = int(input("Enter range : "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")

for i in range(user_input, 0, -1):
    print(i)