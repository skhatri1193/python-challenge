import os
from csv import reader

# Reading in File (NOTE: no matter what I tried, I was not able to use relative path to get the csv to read. 
# I have no problems with getting the in-class activity files to open with relative path, however for this assignment I was not able to despite countless troubleshooting.)
# If required, I can rewrite script to account for general path but I will not be able to load the file myself.

opened_file = open(r"C:\Users\Shari\Desktop\Data Science Course\Challenges\python-challenge\PyPoll\Resources\election_data.csv")
read_file = reader(opened_file)
election_data = list(read_file)

# Initializing Variables

#List for each column
ballot_id = []
county = []
candidates = []

# Initial vote counts
ccs_votes = 0 
dg_votes = 0
rad_votes = 0
winner = ""


# Filling in lists for each column and tallying up votes for each candidate


for row in election_data[1:]:
    # Filling in lists for each column
    ballot_id.append(row[0])
    county.append(row[1])
    candidates.append(row[2])
    # Tallying up votes for each candidate
    if row[2] == "Charles Casper Stockham":
        ccs_votes += 1
    elif row[2] == "Diana DeGette":
        dg_votes += 1
    elif row[2] == "Raymon Anthony Doane":
        rad_votes +=1

# Check to make sure we have accounted for all candidates
unique_canditates = list(set(candidates))

# Total votes in election
total_votes = len(ballot_id)

# Percentage of votes for each candidate
ccs_percent = round((ccs_votes / total_votes) * 100,3)
dg_percent = round((dg_votes / total_votes) * 100,3)
rad_percent = round((rad_votes / total_votes) * 100,3)

# Determining winner of election

# Finds max between the tallying results
max_votes = max(ccs_votes,dg_votes,rad_votes)

# Conditions to determine winner variable
if max_votes == ccs_votes:
    winner = "Charles Casper Stockham"
elif max_votes == dg_votes:
    winner = "Diana DeGette"
elif max_votes == rad_votes:
    winner = "Raymon Anthony Doane"

# Displaying results to terminal
print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_votes}')
print("--------------------------")
print(f'Charles Casper Stockham: {ccs_percent}% ({ccs_votes})')
print(f'Diana DeGette: {dg_percent}% ({dg_votes})')
print(f'Raymon Anthony Doane: {rad_percent}% ({rad_votes})')
print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")

# Exporting results to PyPoll_Anaylsis.txt
report = open('PyPoll_Analysis.txt','w')

report.write("Election Results" + '\n')
report.write("--------------------------" + '\n')
report.write(f'Total Votes: {total_votes}' + '\n')
report.write("--------------------------" + '\n')
report.write(f'Charles Casper Stockham: {ccs_percent}% ({ccs_votes})' + '\n')
report.write(f'Diana DeGette: {dg_percent}% ({dg_votes})' + '\n')
report.write(f'Raymon Anthony Doane: {rad_percent}% ({rad_votes})' + '\n')
report.write("--------------------------" + '\n')
report.write(f'Winner: {winner}' + '\n')
report.write("--------------------------" + '\n')

report.close()

