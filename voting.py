voting_age = 18  # Minimum age required for voting

# Accept age from the user
age = int(input("Enter your age: "))

# Check eligibility for voting
if age >= voting_age:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote.")
