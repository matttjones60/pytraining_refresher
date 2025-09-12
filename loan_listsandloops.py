# Get details of loan
money_owed = float(input("Enter the amount of money owed: ")) # £50,000
interest_rate = float(input("Enter the interest rate (as a percentage): ")) # 3
payment = float(input("Enter the monthly payment: ")) # £1,000
months = 54

monthly_interest_rate = interest_rate / 100 / 12

for i in range(months):
    # Calculate interest to pay
    interest_paid = monthly_interest_rate * money_owed

    # Add interest to money owed
    money_owed = money_owed + interest_paid

    if (money_owed - payment <= 0):
        print('Final payment of', money_owed)
        print('Loan paid off in', i+1, 'months')
        break

    # Make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest')
    print('Money owed is now', money_owed)