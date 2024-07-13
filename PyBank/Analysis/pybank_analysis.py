from csv import reader
import os
from pathlib import Path

# Reading in File (NOTE: no matter what I tried, I was not able to use relative path to get the csv to read. 
# I have no problems with getting the in-class activity files to open with relative path, however for this assignment I was not able to despite countless troubleshooting.)
# If required, I can rewrite script to account for general path but I will not be able to load the file myself.

opened_file = open(r"C:\Users\Shari\Desktop\Data Science Course\Challenges\python-challenge\PyBank\Resources\budget_data.csv")

read_file = reader(opened_file)

# Converting read file into a list
budget_data = list(read_file)

# Fetching header row. (Although I did not need to obtain my results)
header_row = budget_data[0]

# Initializing variables
months = []
profit_losses = []

# Creating lists for months and profit/losses
for row in budget_data[1:]:
    months.append(row[0])
    profit_losses.append(int(row[1]))

# Total Months
total_months = len(months)

# Gross Profit
gross_profit = round(sum(profit_losses),2)

# List comprehension to create list of changes month to month
changes = [profit_losses[i] - profit_losses[i-1] for i in range(1,len(profit_losses))]

# Anaylsis of month to month changes
avg_changes = round((sum(changes) / len(changes)),2) 
max_changes = max(changes)
min_changes = min(changes)

# Finding associated month with greatest increase and decrease in profits
max_month = months[(changes.index(max_changes))+1]
min_month = months[(changes.index(min_changes))+1]

# Printing Results to terminal
print("Financial Analysis")
print("")
print("--------------------------")
print("")
print(f'Total Months: {total_months}')
print(f'Total: ${gross_profit}')
print(f'Average Change: ${avg_changes}')
print(f'Greatest Increase in Profits: {max_month} (${max_changes})')
print(f'Greatest Decrease in Profits: {min_month} (${min_changes})')

# Creating txt file of analysis
report = open('PyBank_Analysis.txt','w')

report.write("Financial Analysis" + '\n')
report.write("" + '\n')
report.write("--------------------------" + '\n')
report.write("" + '\n')
report.write(f'Total Months: {total_months}' + '\n')
report.write(f'Total: ${gross_profit}' + '\n')
report.write(f'Average Change: ${avg_changes}' + '\n')
report.write(f'Greatest Increase in Profits: {max_month} (${max_changes})' + '\n')
report.write(f'Greatest Decrease in Profits: {min_month} (${min_changes})' + '\n')

report.close()






