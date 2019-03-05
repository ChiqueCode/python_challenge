import os
import csv

total_votes = 0
candidate_options = []
candidates_votes = {}
candidate_winner = ""
winning_count = 0
percentage = []
count_candidates = 0
sum = 0



pypoll = os.path.join("Resources", "election_data.csv")
with open(pypoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        #calculating total votes
        total_votes = total_votes + 1
        # dictionary for each candidate and num of votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidates_votes[candidate_name] = 0
        candidates_votes[candidate_name] += 1 

    #finding the percentage for each candidate's votes        
    for (key, value) in candidates_votes.items(): sum += value
    percentage = candidates_votes['Khan'] / (sum + 0.0)
    #percentage = candidates_votes['O'Tooley'] / (sum + 0.0)
    #for (key, value) in candidates_votes.items(): sum += value
    #percentage = candidates_votes['Correy'] / (sum + 0.0)
    #percentage = candidates_votes['Li'] / (sum + 0.0)
    #print "percentage of '%s' is %.2f %%" % ('a' , percentage*100)
    
print("Total Votes: " + str(total_votes))
print("Candidates are: " + str(candidates_votes))
print "Percentage of '%s' is %.2f %%" % ('Votes for Khan' , percentage*100) 
#print "Percentage of '%s' is %.2f %%" % ('Votes for Correy' , percentage*100) 
#print "Percentage of '%s' is %.2f %%" % ('Votes for Li' , percentage*100) 





print("The Winner is: " + max(candidates_votes, key=candidates_votes.get))

#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan