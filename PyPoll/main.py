import csv
import os
# Declare variables
electionData = []
candidates = []
votes = []
totalList =[]
percentList = []
electSummary = []
totalKhan = 0
totalCorrey = 0
totalLi = 0
totalOtooley = 0

# Open budget_data.csv
with open('election_data.csv','r') as csvfile:
# read file budge_data.csv
    csvreader = csv.reader(csvfile,delimiter=',')
# Skip first line
    header = next(csvreader)
# Get unique candidates
    for row in csvreader:
        electionData.append(row)
        votes.append(1)
        if row[2] not in candidates:
            candidates.append(row[2])
    candidateList = candidates
    totalVotes = sum(votes)
    for Khan in electionData:
        if 'Khan' == Khan[2]:
            totalKhan += 1
    for Correy in electionData:
        if 'Correy' == Correy[2]:
            totalCorrey += 1
    for Li in electionData:
        if 'Li' == Li[2]:
            totalLi += 1
    for Otooley in electionData:
        if 'O\'Tooley' == Otooley[2]:
            totalOtooley += 1
    percentKhan = totalKhan / totalVotes
    percentCorrey = totalCorrey / totalVotes
    percentLi = totalLi / totalVotes
    percentOtooley = totalOtooley / totalVotes
    totalList = [totalKhan,totalCorrey,totalLi,totalOtooley]
    percentList = [percentKhan,percentCorrey,percentLi,percentOtooley]
    maxTotal = max(totalList)
    for x in zip(candidates,percentList,totalList):
        if maxTotal == x[2]:
            winner = x[0]
    print("Election Results")
    print("--------------------------------------------")
    print("Total Votes: "+str(totalVotes))
    print("--------------------------------------------")
    for c,p,t in zip(candidates,percentList,totalList):
        summaryResults = "".join(c+" "+str(round(p*100,2))+"00% "+str(t))
        print(summaryResults)
    print("--------------------------------------------")
    print("Winner: "+winner)
    print("--------------------------------------------")

# Export to text file
file = open("election_summary.txt","w")

file.write("Election Results\n")
file.write("--------------------------------------------\n")
file.write("Total Votes: "+str(totalVotes)+"\n")
file.write("--------------------------------------------\n")
for c,p,t in zip(candidates,percentList,totalList):
    summaryResults = "".join(c+" "+str(round(p*100,2))+"00% "+str(t))
    file.write(summaryResults+"\n")
file.write("--------------------------------------------\n")
file.write("Winner: "+winner+"\n")
file.write("--------------------------------------------\n")
