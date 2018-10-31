account_balance = 16000

print("*********************************")
print("Welcome to HW Bank Sending ...")
print("***************************8*****")

amount_to_send = int(input("Enter amount to send: "))

# 1st Range of Bank Charges and Tax
if amount_to_send >=500 and amount_to_send <=2500 :
  bank_charge = 300
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))

# 2th Range of Bank Charges and Tax
if amount_to_send >=2501 and amount_to_send <=5000 :
  bank_charge = 550
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 3rd Range of Bank Charges and Tax
if amount_to_send >=5001 and amount_to_send <=15000 :
  bank_charge = 1050
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


  # 4th Range of Bank Charges and Tax
if amount_to_send >=15001 and amount_to_send <=30000 :
  bank_charge = 1050
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 5th Range of Bank Charges and Tax
if amount_to_send >=30001 and amount_to_send <=45000 :
  bank_charge = 1050
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 6th Range of Bank Charges and Tax
if amount_to_send >=45001 and amount_to_send <=60000 :
  bank_charge = 1050
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))

# 7th Range of Bank Charges and Tax
if amount_to_send >=60001 and amount_to_send <=125000 :
  bank_charge = 1610
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 8th Range of Bank Charges and Tax
if amount_to_send >=125001 and amount_to_send <=250000 :
  bank_charge = 1610
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 9th Range of Bank Charges and Tax
if amount_to_send >=250001 and amount_to_send <=500000 :
  bank_charge = 1610
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 10th Range of Bank Charges and Tax
if amount_to_send >=500001 and amount_to_send <=1000000 :
  bank_charge = 2020
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 11th Range of Bank Charges and Tax
if amount_to_send >=1000001 and amount_to_send <=2000000 :
  bank_charge = 2020
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 12th Range of Bank Charges and Tax
if amount_to_send >=2000001 and amount_to_send <=4000000 :
  bank_charge = 2020
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))


# 12th Range of Bank Charges and Tax
if amount_to_send >=4000001 and amount_to_send <=7000000 :
  bank_charge = 2020
  taxes = (0.01 * amount_to_send)
  total_charges = bank_charge + taxes
  sending_including_charges = total_charges + amount_to_send

  print(f"For the recipent to receive {amount_to_send} UGX, deposit {int(sending_including_charges)}")

  final_amount_to_send = int(input("Enter the final amount to send: "))



# sending money
if account_balance >= final_amount_to_send:
  # Sending Variable
  account_balance = account_balance - final_amount_to_send

  print(f"You have send {final_amount_to_send} UGX ")
  print(f"Your new account balance is {account_balance} UGX")

else:
  print("insufficient funds")

"""
**********************************************
            Sending Money Ends
**********************************************
"""