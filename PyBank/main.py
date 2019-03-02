# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#import the dependancies
import os
import csv

total_months = 0
total_profit = 0
total_profit_list = []
revenue_change = 0
revenue_change_list = []
month_of_change = []

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader: 
        total_months = total_months + 1
        total_profit = total_profit + abs(int(row[1]))
        total_profit_list.append(row[1])
        
    revenue_change = total_profit / total_months

print("Total Months: " + str(total_months))  
print("Total Profit: " + str(total_profit))
print("Average Change: " + str(revenue_change))
print(max(total_profit_list))
print(min(total_profit_list))

  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
