while True:
    try:
        user_input = int(input("Enter a number : "))
        break
    except ValueError:
        print("Invalid input. Please enter a number")

for i in range(1, user_input + 1):
    if user_input % i == 0:
        print(i)