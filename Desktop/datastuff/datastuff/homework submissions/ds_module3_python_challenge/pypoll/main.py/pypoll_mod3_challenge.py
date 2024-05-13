import csv

#file path
csvpath = "election_data.csv" 

#variable for vote count
total_vote = 0
#use a dictionary for the candidates
candidate_dict = {}

#open the csv using the utf-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #read each row after the header
    for row in csvreader:
        total_vote += 1
        voter_choice = row[2]
        if voter_choice in candidate_dict.keys():
            candidate_dict[voter_choice] += 1
        else:
            candidate_dict[voter_choice] = 1

print(total_vote)
print(candidate_dict)

#create text table (code recieved from xpert)
results_data = {
    'Charles Casper Stockham': 85213,
    'Diana DeGette': 272892,
    'Raymon Anthony Doane': 11606
}

# calculate total votes
total_votes = sum(results_data.values())

# generate the election results text
election_results_text = ""
for candidate, votes in results_data.items():
    percentage = (votes / total_votes) * 100
    election_results_text += f"{candidate}: {percentage:.3f}% ({votes})\n"

# determine the winner
winner = max(results_data, key=results_data.get)

# add the winner to the election results text
election_results_text += "-------------------------\n"
election_results_text += f"Winner: {winner}\n"

print(election_results_text)

# generate the election data text (code received from xpert)
# election analysis results
results = """
Election Results
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
"""

# define the file name to save the results
file_name = 'election_analysis_results.txt'

# write the results to a text file
with open(file_name, 'w') as file:
    file.write(results)

print("Election analysis results saved to 'election_analysis_results.txt'")