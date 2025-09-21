# finance_calculator.py

# Prompt user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

# Prompt user for their monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings (Income - Expenses)
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a 5% simple interest
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")