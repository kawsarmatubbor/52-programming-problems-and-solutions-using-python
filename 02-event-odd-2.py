user_input = input("Enter a number : ")

last_number = int(user_input[-1])

if last_number % 2 == 0:
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")