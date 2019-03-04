# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#import the dependancies
import os
import csv

total_months = 0
total_profit = 0
total_profit_list = []
average_change = 0
monthly_change_list = []
month_of_change = []
prev_revenue = 0
monthly_change = 0
gt_revenue_increase = 0
gt_revenue_increase_month = ""
gt_revenue_decrease = 0
gt_revenue_decrease_month = ""

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader: 
        total_months = total_months + 1
        total_profit = total_profit + (int(row[1]))
        #calculating monthly change
        monthly_change = int(row[1]) - prev_revenue 
        monthly_change_list.append(monthly_change)
        prev_revenue = int(row[1])
        #calculating greatest increase
        if monthly_change > gt_revenue_increase:
            gt_revenue_increase = monthly_change
            gt_revenue_increase_month = row[0]
       #calculatiing greatest decrease
        if monthly_change < gt_revenue_decrease:
           gt_revenue_decrease = monthly_change
           gt_revenue_decrease_month = row[0]


    monthly_change_list = monthly_change_list[1:]
    
    average_change = sum(monthly_change_list) / len(monthly_change_list)
        

print("Total Months: " + str(total_months))  
print("Total Profit: " + str(total_profit))
print("Average Change: " + str(average_change))
print("The Greatest Increase is " + str(gt_revenue_increase) + " in " + str(gt_revenue_increase_month))
print("The Greatest Decrease is" + str(gt_revenue_decrease) + "in " + str(gt_revenue_decrease_month))
#print(min(total_profit_list))

  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
