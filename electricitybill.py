# Accept the number of units from the user
units = int(input("Enter the number of units consumed: "))

# Initialize variables for the bill amount and unit prices
bill_amount = 0
price_first_100_units = 0
price_next_100_units = 5
price_after_200_units = 10

# Calculate the bill amount based on the number of units consumed
if units <= 100:
    bill_amount = 0
elif units <= 200:
    bill_amount = (units - 100) * price_next_100_units
elif units > 200:
    bill_amount = 100 * price_next_100_units + (units - 200) * price_after_200_units

# Display the bill amount
print("The electricity bill amount is: Rs", bill_amount)
