import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
        
    for row_count, row in enumerate(csvreader, start=1):
        budget = int(row['Profit/Losses'])
        totals.append(budget)
        avg = sum(totals) / row_count


# The greatest increase in profits (date and amount) over the entire period
       
Greatest = max(totals)
Decrease = min(totals)

with open(budget_csv, 'r') as csvfile:
   csvreader = csv.DictReader(csvfile, delimiter=",")
   for row_count, row in enumerate(csvreader, start=1):
       if int(row['Profit/Losses']) == Greatest:
            Greatest =  int(row['Profit/Losses'])
            date = (row['Date'])
# The greatest decrease in losses (date and amount) over the entire period
       if int(row['Profit/Losses']) == Decrease:
            Decrease =  int(row['Profit/Losses'])
            date1 = (row['Date'])
           
# Screen Financial Analysis Ouput

print ("Financial Analysis")
print ("--------------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: ${}".format(sum(totals)))
print ("Average Change: $", format(avg, ",.2f"))
print ("Greatest Increase in Profits: ", (date),"$", (Greatest))
print ("Greatest Decrease in Profits: ", (date1),"$", (Decrease))


output_file = os.path.join("Financial Analysis Report.txt")

#  Writing the output file
with open(output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-------------------------------\n")
    text_file.write (("Total Months: {}\n".format(row_count)))    
    text_file.write ("Total: ${}\n".format(sum(totals)))
    text_file.write ("Average Change: ${}\n".format(avg))
    text_file.write ("Greatest Increase in Profits: ${}\n".format(max(totals)))
    text_file.write ("Greatest Decrease in Profits: ${}\n".format(min(totals)))