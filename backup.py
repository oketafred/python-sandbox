# Author: Oketa Fred
# Laboremus Uganda Home Assignment

# Object Definition
class Account:
  # Declaring a constructor Method
  def __init__(self, balance = 0):
    # self.owner = owner
    self.balance = balance
    self.pin = 1234

  # A Method for Depositing Money in their account
  def deposit(self, deposit_amount):
    self.balance = self.balance + deposit_amount
    print(f"You have deposited {deposit_amount} in your account")
    print(f"You new account balance is {self.balance}")

  # A Method for Withdrawing Money from their account
  def withdrawal(self, withdrawal_amount):
    if self.balance >= withdrawal_amount:
      self.balance = self.balance - withdrawal_amount
      print(f"You have withdrawn {withdrawal_amount}")
    else:
      print("Insufficient Fund")

  # A Method for checking account balance
  def check_account_balance(self):
    print(f"Your account balance is {self.balance}")

# Object Creation or Instance of a class
a = Account()


# The Main Menu Function
def main_menu():
  print("--------------------------------")
  print("Welcome to HW MicroFinance Bank")
  print("--------------------------------")
  user_input = input("Enter d to deposit, w to withdraw and q to exit: ")

  while user_input != "q":
    if user_input == "d":
      deposit_amount = int(input("Enter amount to deposit: "))
      a.deposit(deposit_amount)
    elif user_input == "b":
      a.check_account_balance()
    elif user_input == "w":
      withdrawal_amount = int(input("Enter amount to withdraw: "))
      a.withdrawal(withdrawal_amount)
    else: 
      print("\nPlease check your input and try again")
    user_input = input("\n Enter d to deposit, w to withdraw and q to exit: ")


def login():
  user_pin = int(input("Please enter your pin: "))

  if user_pin == a.pin:
    main_menu()
  else:
    print("Please check your PIN number: ")



# main_menu()
login()




# account_owner_name = input("Enter your Full Name: ")
# deposit_amount = int(input("Enter amount to deposit: "))
# a = Account("Oketa", 500)

# a.deposit(deposit_amount)


# print("Welcome to HW MicroFinance Bank")