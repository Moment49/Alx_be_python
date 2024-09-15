monthly_income = float(input("Enter your monthly income: "))
total_monthly_expense = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expense
print(monthly_savings)
rate = 0.05
time = 12
projected_savings = monthly_savings * time + (monthly_savings * time * rate)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
