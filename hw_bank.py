def main_menu():
  user_input = input("Enter d to deposit, w to withdraw and q to exit: ")

  if user_input == "d":
    deposit()
  elif user_input == "w":
    withdraw()
  else: 
    print("\nPlease check your input and try again")
    user_input = input("Enter d to deposit, w to withdraw and q to exit: ")


main_menu()