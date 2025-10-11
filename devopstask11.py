# Ask the user for initial balance and deposit amount
initial_balance = float(input("Enter your initial balance: "))
deposit_amount = float(input("Enter the deposit amount: "))

# Calculate updated balance
updated_balance = initial_balance + deposit_amount

# Display the result
print(f"Your updated balance is: ₹{updated_balance:.2f}")