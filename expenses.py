expenses = [2200, 2350, 2600, 2130, 2190, 10.50, 1980]

sum = int(0)

for x in expenses:
    sum = sum + x
#you can also use the built-in sum() function to get the total of a list
#sum = sum(expenses)

print("Total expenses: " + str(sum))

if sum > 14000:
    print("You spent more than 2000 in February YOU'RE FIRED")
else:
    print("You are within the budget for February")