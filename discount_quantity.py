# Accept the quantity from the user
quantity = int(input("Enter the quantity purchased: "))

# Calculate the cost
# For simplicity, let's assume the cost per item is 100
cost = quantity * 100

# Check if the cost exceeds 1000
if cost > 1000:
    # Apply a discount of 10%
    discount = 0.1 * cost
    discounted_cost = cost - discount
    print("Discounted cost:", discounted_cost)
else:
    print("Cost:", cost)
