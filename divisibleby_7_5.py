numbers = []
for num in range(1500, 2701):

    if num % 7 == 0 and num % 5 == 0:
        # Append the number to the list
        numbers.append(num)

print(numbers)
