# Get loan details
money_owed = float(input("Money owed in dollars: "))
apr = float(input("Enter Annual Percentage Rate: "))
payment = float(input("Monthly payment in dollars: "))
months = int(input("Enter number of months to see results for: "))

# Convert APR to percentage then divide by 12
monthly_rate = apr / 100  / 12

for i in range(months):
    # Add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in {} months".format(i+1))
        break

    # Make payment
    money_owed = money_owed - payment

    # Print results
    print("Paid {} of which {} was interest. Now I owe {}".format(payment, interest_paid, money_owed))