balance = float(input("Enter your balance: "))
deposit = float(input("Enter deposit amount: "))
new_balance = balance + deposit
print("The updated account balance:", new_balance)
withdrawal = float(input("Enter withdrawal amount: "))
updated_balance = new_balance - withdrawal
print("The updated account balance after withdrawal:", updated_balance)