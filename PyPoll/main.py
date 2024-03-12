# import modules
import os
import csv

# Define the path to the csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the csv file
with open(csvpath) as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Skip the header row
    next(csvreader, None)

    # Loop through each row in the csv
    for row in csvreader:
        total_votes += 1  # Calculate total votes
        candidate_name = row[2] # pull candidate name

# Print output
print("Election Results")
print("------------")
print(f"Total Votes: {total_votes}")
print("------------")


# Export analysis to txt file
output_path = os.path.join('PyPoll','Analysis', 'analysis.txt') # set output path


with open(output_path, 'w') as file:
    file.write("Election Results")
    file.write("------------")
    file.write(f"Total Votes: {total_votes}")
    file.write("------------")