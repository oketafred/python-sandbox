# Author: Oketa Fred
# Laboremus Uganda Home Assignment

# Object Definition
class Account:
  # Declaring a constructor Method
  def __init__(self, balance = 0):
    self.balance = balance
    self.pin = "1234"

  # A Method for Depositing Money in their account
  def deposit(self, deposit_amount):
    self.balance = self.balance + deposit_amount
    print(f"You have deposited {deposit_amount} UGX")
    print(f"You new account balance is {self.balance} UGX")

  # A Method for Withdrawing Money from their account
  def withdrawal(self, withdrawal_amount):
    # First Range of Bank Charges and Tax
    if withdrawal_amount <=499:
      print("Minimum transaction is 500")
    elif withdrawal_amount >=500 and withdrawal_amount <=2500 :
      bank_charge = 300
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Second Range of Bank Charges and Tax
    elif withdrawal_amount >=2501 and withdrawal_amount <=5000 :
      bank_charge = 550
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Third Range of Bank Charges and Tax
    elif withdrawal_amount >=5001 and withdrawal_amount <=15000 :
      bank_charge = 1050
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Fourth Range of Bank Charges and Tax
    elif withdrawal_amount >=15001 and withdrawal_amount <=30000 :
      bank_charge = 1050
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
      else: 
        print("insufficent funds")

    # Fifth Range of Bank Charges and Tax
    elif withdrawal_amount >=30001 and withdrawal_amount <=45000 :
      bank_charge = 1050
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Sixth Range of Bank Charges and Tax
    elif withdrawal_amount >=45001 and withdrawal_amount <=60000 :
      bank_charge = 1050
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")

    # Seventh Range of Bank Charges and Tax
    elif withdrawal_amount >=60001 and withdrawal_amount <=125000 :
      bank_charge = 1610
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")

    # Eighth Range of Bank Charges and Tax
    elif withdrawal_amount >=120001 and withdrawal_amount <=250000 :
      bank_charge = 1610
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Nineth Range of Bank Charges and Tax
    elif withdrawal_amount >=250001 and withdrawal_amount <=500000 :
      bank_charge = 1610
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Tenth Range of Bank Charges and Tax
    elif withdrawal_amount >=500001 and withdrawal_amount <=1000000 :
      bank_charge = 2020
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # Eleventh Range of Bank Charges and Tax
    elif withdrawal_amount >=1000001 and withdrawal_amount <=2000000 :
      bank_charge = 2020
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # 12th Range of Bank Charges and Tax
    elif withdrawal_amount >=2000001 and withdrawal_amount <=4000000 :
      bank_charge = 2020
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")


    # 13th Range of Bank Charges and Tax
    elif withdrawal_amount >=4000001 and withdrawal_amount <=7000000 :
      bank_charge = 2020
      taxes = (0.01 * withdrawal_amount)
      total_charges = bank_charge + taxes
      withdraw_including_charges = total_charges + withdrawal_amount

      if self.balance >= withdraw_including_charges:
        self.balance = self.balance - withdrawal_amount
        self.balance = self.balance - total_charges
        print(f"You have withdrawn {withdrawal_amount} UGX")
        print(f"Bank Charge of {bank_charge} UGX and tax of {taxes} UGX")
        print(f"Your new account balance is {self.balance} UGX")
      else: 
        print("insufficent funds")

    else:
      print("Minimum Transaction is 7000000 UGX")

  # A Method for checking account balance
  def check_account_balance(self):
    print(f"Your account balance is {self.balance} UGX")


  # Method for sending Money
  def sending_money(self, amount_to_send):
    # Stating point for sending money
    # 1st Range of Bank Charges and Tax
    if amount_to_send >= 0 and amount_to_send <500:

      print("Minimum Transaction is 500")
    
    elif amount_to_send >=500 and amount_to_send <=2500 :
      bank_charge = 300
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 2th Range of Bank Charges and Tax
    elif amount_to_send >=2501 and amount_to_send <=5000 :
      bank_charge = 550
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 3rd Range of Bank Charges and Tax
    elif amount_to_send >=5001 and amount_to_send <=15000 :
      bank_charge = 1050
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


      # 4th Range of Bank Charges and Tax
    elif amount_to_send >=15001 and amount_to_send <=30000 :
      bank_charge = 1050
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 5th Range of Bank Charges and Tax
    elif amount_to_send >=30001 and amount_to_send <=45000 :
      bank_charge = 1050
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 6th Range of Bank Charges and Tax
    elif amount_to_send >=45001 and amount_to_send <=60000 :
      bank_charge = 1050
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")

    # 7th Range of Bank Charges and Tax
    elif amount_to_send >=60001 and amount_to_send <=125000 :
      bank_charge = 1610
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 8th Range of Bank Charges and Tax
    elif amount_to_send >=125001 and amount_to_send <=250000 :
      bank_charge = 1610
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 9th Range of Bank Charges and Tax
    elif amount_to_send >=250001 and amount_to_send <=500000 :
      bank_charge = 1610
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 10th Range of Bank Charges and Tax
    elif amount_to_send >=500001 and amount_to_send <=1000000 :
      bank_charge = 2020
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 11th Range of Bank Charges and Tax
    elif amount_to_send >=1000001 and amount_to_send <=2000000 :
      bank_charge = 2020
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")


    # 12th Range of Bank Charges and Tax
    elif amount_to_send >=2000001 and amount_to_send <=4000000 :
      bank_charge = 2020
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")



    # 13th Range of Bank Charges and Tax
    elif amount_to_send >=4000001 and amount_to_send <=7000000 :
      bank_charge = 2020
      taxes = (0.01 * amount_to_send)
      total_charges = bank_charge + taxes
      sending_including_charges = total_charges + amount_to_send

      if self.balance >= sending_including_charges:
        print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")
      
      else:
        print("insufficient funds")

    elif amount_to_send >= 7000001:
      print("Maximum Transaction is 7000000 UGX")

  # Sending Money End Here
"""
***************************************************************************** 
End of the Account Class 
*****************************************************************************
"""

# Object Creation or Instance of a class
a = Account()


# The Main Menu Function
def main_menu():
  print("--------------------------------")
  print("Welcome to HW MicroFinance Bank")
  print("--------------------------------")
  user_input = input("Enter d to deposit, w to withdraw, b to check balance, s to send money and q to exit: ")

  while user_input != "q":
    if user_input == "d":
      deposit_amount = int(input("Enter amount to deposit: "))
      a.deposit(deposit_amount)
    elif user_input == "b":
      a.check_account_balance()
    elif user_input == "w":
      withdrawal_amount = int(input("Enter amount to withdraw: "))
      a.withdrawal(withdrawal_amount)
    elif user_input == "s":
      final_amount_to_send = int(input("Enter amount to send: "))
      a.sending_money(final_amount_to_send)
    else: 
      print("\nPlease check your input and try again")
    user_input = input("\nEnter d to deposit, w to withdraw, b to check balance, s to send money and q to exit: ")


# Login Function
def login():
  # Getting your PIN Number
  user_pin = input("Please enter your PIN: ")

  if user_pin == a.pin:
    # Executing the Main Menu Function if the PIN is correct
    main_menu()
  else:
    print("Please check your PIN number: ")
    user_pin = input("Please enter your PIN: ")
    if user_pin == a.pin:
      # Executing the Main Menu Function if the PIN is correct
      main_menu()


# Executing the Login Function where the user can enter the PIN
login()

