
  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

#import the dependancies
import os
import csv

total_months = 0
total_profit = 0

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader: 
        data = list(csvreader)
        row_count = len(data)
        #total_profit = sum(int(row[1]) for row in csv.reader(csvfile))
        total_profit = total_profit + int(row[1])

#def get_averages(csvpath):
    #column_sums = None
    #with open(csvpath) as file:
        #lines = file.readlines()
        #rows_of_numbers = [map(float, line.split(',')) for line in lines]
        #sums = map(sum, zip(*rows_of_numbers))
        #averages = [sum_item / len(lines) for sum_item in sums]
        #return averages

#print(get_averages(csvpath))








print("Total Months: " + str(row_count))  
print("Total Profit: " + str(total_profit))



  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
