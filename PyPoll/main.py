#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

total_votes = 0
candidate_options = []
candidates_votes = {}
candidate_winner = ""
winning_count = 0


pypoll = os.path.join("Resources", "election_data.csv")
with open(pypoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #calculating total votes
        total_votes = total_votes + 1
        # adding every candidate to the list
        #output.append(row[2]) 
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] += 1
    print(candidates_votes)
        #if row[2] not in candidates:
            #candidates.append(row[2])
            #index = candidates.index(row[2])
            #num_votes.append(1)
        #else:
            #index = candidates.index(row[2])
            #num_votes[index] += 1

# looping through the rows to find unique values = candidates
    #f#or x in output:
        #if x not in output:
            #unique.append(x)
   # print(unique)            
    
print("Total Votes: " + str(total_votes))
#print(candidates)


        










#Election Results
#-------------------------
#otal Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan