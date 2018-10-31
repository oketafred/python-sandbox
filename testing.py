account_balance = 16000

print("*********************************")
print("Welcome to HW Bank Withdrawal ...")
print("***************************8*****")

Withdrawal_amount = int(input("Enter amount to withdraw: "))

# First Range of Bank Charges and Tax
if Withdrawal_amount >=500 and Withdrawal_amount <=2500 :
  bank_charge = 300
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Second Range of Bank Charges and Tax
if Withdrawal_amount >=2501 and Withdrawal_amount <=5000 :
  bank_charge = 550
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Third Range of Bank Charges and Tax
if Withdrawal_amount >=5001 and Withdrawal_amount <=15000 :
  bank_charge = 1050
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Fourth Range of Bank Charges and Tax
if Withdrawal_amount >=15001 and Withdrawal_amount <=30000 :
  bank_charge = 1050
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")

# Fifth Range of Bank Charges and Tax
if Withdrawal_amount >=30001 and Withdrawal_amount <=45000 :
  bank_charge = 1050
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Sixth Range of Bank Charges and Tax
if Withdrawal_amount >=45001 and Withdrawal_amount <=60000 :
  bank_charge = 1050
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")

# Seventh Range of Bank Charges and Tax
if Withdrawal_amount >=60001 and Withdrawal_amount <=125000 :
  bank_charge = 1610
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")

# Eighth Range of Bank Charges and Tax
if Withdrawal_amount >=120001 and Withdrawal_amount <=250000 :
  bank_charge = 1610
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Nineth Range of Bank Charges and Tax
if Withdrawal_amount >=250001 and Withdrawal_amount <=500000 :
  bank_charge = 1610
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Tenth Range of Bank Charges and Tax
if Withdrawal_amount >=500001 and Withdrawal_amount <=1000000 :
  bank_charge = 2020
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# Eleventh Range of Bank Charges and Tax
if Withdrawal_amount >=1000001 and Withdrawal_amount <=2000000 :
  bank_charge = 2020
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# 12th Range of Bank Charges and Tax
if Withdrawal_amount >=2000001 and Withdrawal_amount <=4000000 :
  bank_charge = 2020
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")


# 13th Range of Bank Charges and Tax
if Withdrawal_amount >=4000001 and Withdrawal_amount <=7000000 :
  bank_charge = 2020
  taxes = (0.01 * Withdrawal_amount)
  total_charges = bank_charge + taxes
  withdraw_including_charges = total_charges + Withdrawal_amount

  if account_balance > withdraw_including_charges:
    account_balance = account_balance - Withdrawal_amount
    print(f"You have withdrawn {Withdrawal_amount}")
    print(f"Bank Charge of {bank_charge} and tax of {taxes}")
  else: 
    print("insufficent funds")
