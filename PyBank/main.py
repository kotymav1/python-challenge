# import modules
import os
import csv

# Define the path to the csv file
csvpath = os.path.join('PyBank','Resources','budget_data.csv')

# Initialize variables
total_months = 0
total = 0
total_change = 0
average_change = 0
greatest_profit_increase = ['', 0]  # Will hold the month and the amount of the greatest increase
greatest_profit_decrease = ['', float('inf')]  # Will hold the month and the amount of the greatest decrease
previous_amount = None  # Initialize previous_amount as None for the first iteration

# Open and read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Skip the header row
    next(csvreader, None)

    # Loop through each row in the csv
    for row in csvreader:
        total_months += 1  # Calculate total months
        current_amount = int(row[1])  # Get the current row's profit/loss amount
        total += current_amount  # Calculate total net profit

        # Calculate change from previous month if previous_amount is not None
        if previous_amount is not None:
            change = current_amount - previous_amount
            total_change += change  # Add the change to total_change

            # Check for greatest increase
            if change > greatest_profit_increase[1]:
                greatest_profit_increase = [row[0], change]

            # Check for greatest decrease
            if change < greatest_profit_decrease[1]:
                greatest_profit_decrease = [row[0], change]

        previous_amount = current_amount  # Set previous_amount to current_amount for next iteration

# Calculate average change, but subtract 1 from total_months to account for the first month
if total_months > 1:
    average_change = total_change / (total_months - 1)

# Print the analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]})")

# Export analysis to txt file
output_path = os.path.join('PyBank','Analysis', 'analysis.txt') # set output path


with open(output_path, 'w') as file:
    file.write("Financial Analysis")
    file.write("-----------------------------")
    file.write(f"Total Months: {total_months}")
    file.write(f"Total: ${total}")
    file.write(f"Average Change: ${average_change:.2f}")
    file.write(f"Greatest Increase in Profits: {greatest_profit_increase[0]} (${greatest_profit_increase[1]})")
    file.write(f"Greatest Decrease in Profits: {greatest_profit_decrease[0]} (${greatest_profit_decrease[1]})")