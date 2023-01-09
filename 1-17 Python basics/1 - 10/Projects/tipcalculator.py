print("Welcome to the tip calculator.")

#inputting data
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_customers = int(input("How many people to split the bill? "))

#rounding to 2 decimals, but not formatting
bill_per_customer = round(bill / num_of_customers * (1 + tip/100), 2)

#formatting to get 2 decimals always
bill_per_customer_formatted = "{:0.2f}".format(bill_per_customer)

print(f"Each person should pay: ${bill_per_customer_formatted}")
