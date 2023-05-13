import math

print('''Please choose which calculation you would like to complete:

investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
''')

calculation = input("Please enter either 'investment' or 'bond' to proceed: ").lower()

print(calculation)
print()
while calculation != "investment" and calculation != "bond":
    calculation = input("Invalid option input! Please enter either 'investment' or 'bond' to proceed: ").lower()

if calculation == "investment":
    deposit = int(input("How much money are you depositing?: "))
    investment_rate = int(input("What is the percentage of the interest rate you are paying?: ")) / 100
    investment_term = int(input("How many years are you planning on investing for?: "))
    interest_type = input("Do you want to choose simple or compound interest?: ").lower()
    while interest_type != "simple" and interest_type != "compound":
        interest_type = input("Invalid option selected! Please enter either simple or compound: ").lower()
    if interest_type == "simple":
        total_amount = deposit * (1 + (investment_rate * investment_term))
        print()
        total_amount_currency = "£{:,.2f}".format(total_amount)
        print(f"The total amount is {total_amount_currency}")
    elif interest_type == "compound":
        total_amount = deposit * math.pow((1 + investment_rate), investment_term)
        print()
        total_amount_currency = "£{:,.2f}".format(total_amount)
        print(f"The total amount is {total_amount_currency}")
elif calculation == "bond":
    house_value = int(input("What is the present value of your house?: "))
    bond_rate = int(input("What interest rate are you paying?: "))
    bond_term = int(input("How many months do you plan to take to repay the bond?: "))
    monthly_interest = (bond_rate / 100)/12
    monthly_repayment = (monthly_interest * house_value)/(1 - ((1 + monthly_interest)**(-bond_term)))
    print()
    monthly_repayment_currency = "£{:,.2f}".format(monthly_repayment)
    print(f"Your monthly repayments will be {monthly_repayment_currency} per month.")