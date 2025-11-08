monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are", monthly_income - monthly_expenses)
print("Projected savings after one year, with interest, is:", monthly_savings * 12 + (monthly_savings * 12 * 0.05))




