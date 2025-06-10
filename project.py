# Personal Budget Tracker


income = input("Enter Your Monthly Income: ")

expence = {}
percentages = {}

categories = ["Rent", "Food", "Entertainment"]
for category in categories:
    money = input(f"Enter your monthly {category} expence: ")
    expence[category] = int(money)
    percentages[category] = (int(money)/int(income)) * 100 


for category, money in expence.items():
    money = expence[category]
    percent = percentages[category]
    # print(f"{category} : {money} ({percent})")



print(f"Income: {income}")

totalExpenses = sum(expence.values())
print(f"Total Expenses: {totalExpenses}")

balance = int(income) - totalExpenses
print(f"Money Left: {balance}")

print(f"{categories[1]} is {percentages[categories[1]]} % of your income")


# print(expence)
# print(percentages[categories[1]])
