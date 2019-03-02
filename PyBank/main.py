  # The average of the changes in months in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

#import the dependancies
import os
import csv

total_months = 0
total_profit = 0
revenue_change = 0
revenue_change_list = []
month_of_change = []

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader: 
        total_months = total_months + 1
        #total_profit = sum(int(row[1]) for row in csv.reader(csvfile))
        total_profit = total_profit + abs(int(row[1]))
        
    revenue_change = total_profit / total_months

        # Take the difference between two months and append to monthly profit change
        #monthly_profit_change = total_profit[row+1] - total_profit[row]
        #previous_revenue = float(row[1])
        #revenue_change = float(row[1])- previous_revenue
        #revenue_change_list = revenue_change_list + [revenue_change]
        #month_of_change = [month_of_change] + [row[0]]
        



print("Total Months: " + str(total_months))  
print("Total Profit: " + str(total_profit))
print("Average Change: " + str(revenue_change))


  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
