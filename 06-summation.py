while True:
    user_input = input("Enter number : ")
    if len(user_input) < 2 :
        print("Enter a large number")
    else:
        break
print(int(user_input[0]) + int(user_input[-1]))