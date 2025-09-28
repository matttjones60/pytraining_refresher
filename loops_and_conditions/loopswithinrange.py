total = 0
expenses = []

for i in range(7):
    expenses.append(float(input("Enter expense for day" + str(i + 1) + ": ")))

total = sum(expenses)

print("Total expenses: " + str(total))
