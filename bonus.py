# Accept the salary and years of service from the user
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Check if the employee is eligible for a bonus
if years_of_service > 5:
    # Calculate the bonus amount
    bonus = 0.05 * salary
    print("Net bonus amount:", bonus)
else:
    print("No bonus")
