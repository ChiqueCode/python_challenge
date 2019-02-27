
  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

#import the dependancies
import os
import csv

#create empty lists 
total_profit = []

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    data = list(csvreader)
    row_count = len(data) 
    print("Total Months: " + str(row_count)) 

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        #total_profit.append(int(row[1]))    

        total_profit = sum(int(row[1] for row in csv.reader(csvfile))
        print(total_profit)     

# print the data
#print("Total profit: " + str(total_profit))

  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)