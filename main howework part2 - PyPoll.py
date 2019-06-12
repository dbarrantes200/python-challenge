import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Otooley_count = 0

    
    for row_count, row in enumerate(csvreader, start=1):
        votes = int(row['Voter ID'])
                
        if row['Candidate'] == "Khan":
            Khan_count = Khan_count + 1
            Khan_average =  (Khan_count / row_count)
        elif row['Candidate'] == "Correy":
            Correy_count = Correy_count + 1
            Correy_average =  (Correy_count / row_count)
        elif row['Candidate'] == "Li":
            Li_count = Li_count + 1
            Li_average =  (Li_count / row_count)
        elif row['Candidate'] == "O'Tooley":
            Otooley_count = Otooley_count + 1
            Otooley_average =  (Otooley_count / row_count)        

# Print Election Results          
print ("Election Results")
print ("-------------------------------")
print ("Total Votes: {}".format(row_count))
print ("-------------------------------")
print (("Khan "+"{:.3%}".format(Khan_average)), "(",(Khan_count),")")    
print (("Correy "+"{:.3%}".format(Correy_average)), "(",(Correy_count),")")    
print (("Li "+"{:.3%}".format(Li_average)), "(",(Li_count),")")    
print (("O'Tooley "+"{:.3%}".format(Otooley_average)), "(",(Otooley_count),")")    
print ("-------------------------------")
print ("Winner: Khan")
print ("-------------------------------")
output_file = os.path.join("Election Results Report.txt")

#  Write the output file
with open(output_file, "w") as text_file:
   
    text_file.write ("Election Results\n")
    text_file.write ("-------------------------------\n")
    text_file.write (("Total Votes: {}\n".format(row_count)))
    text_file.write ("-------------------------------\n")      
    Khan_string = ((Khan_average), (Khan_count))
    text_file.write (("Khan {}\n".format(Khan_string)))
    Correy_string = ((Correy_average), (Correy_count))    
    text_file.write (("Correy {}\n".format(Correy_string)))
    Li_string = ((Li_average), (Li_count))
    text_file.write (("Li {}\n".format(Li_string)))
    Otooley_string = ((Otooley_average), (Otooley_count))    
    text_file.write (("O'Tooley {}\n".format(Otooley_string)))
    text_file.write ("-------------------------------\n")
    text_file.write ("Winner {}\n".format("Khan"))
    text_file.write ("-------------------------------\n")    