import csv
import os

# Declare variables
profitLossList = []
dateList = []
budget = []

# Open budget_data.csv
with open('budget_data.csv','r') as csvfile:
# read file budge_data.csv
    csvreader = csv.reader(csvfile,delimiter=',')
# Skip first line
    header = next(csvreader)
    for row in csvreader:
        profitLossList.append(float(row[1]))
        dateList.append(1)
        budget.append(row)
# Get count of each row that represents each month store in totalMonth variable
    totalMonth = sum(dateList)
# Get sum of all Profit/losses column store in totalProfit
    totalProfit = sum(profitLossList)
# Get average change of Profit/loss which equals MonthDiff / totalMonth store in averageChange
    monthDiff = [profitLossList[i+1]-profitLossList[i] for i in range(len(profitLossList)-1)]
    averageChange = sum(monthDiff)/(totalMonth - 1)
# Find Max profit store Data and profit in profit list variable
    maxProfit = max(monthDiff)
# Find Min Profit store Data and profit in losses list variable
    minLoss = min(monthDiff)
# Find Max and Min Profits
    mxProfit = max(profitLossList)
    mnProfit = min(profitLossList)
# Search for min and max in dataset
    for x in budget:
        if mxProfit == float(x[1]):
            dateMaxProfit = x
        if mnProfit == float(x[1]):
            dateMinLoss = x
# Print to terminal
    print("Total Months: "+ str(totalMonth))
    print("Total: "+ str(int(totalProfit)))
    print("Average Change: " + str(round(averageChange,2)))
    print("Greatest Increase in Profits: "+ str(dateMaxProfit[0]) + " ($"+str(maxProfit)+")")
    print("Greatest Decrease in Profits: "+ str(dateMinLoss[0]) + " ($"+str(minLoss)+")")
# Export to text file
file = open("budget_summary.txt","w")

file.write("Total Months: "+ str(totalMonth)+"\n")
file.write("Total: "+ str(int(totalProfit))+"\n")
file.write("Average Change: " + str(round(averageChange,2))+"\n")
file.write("Greatest Increase in Profits: "+ str(dateMaxProfit[0]) + " ($"+str(maxProfit)+")\n")
file.write("Greatest Decrease in Profits: "+ str(dateMinLoss[0]) + " ($"+str(minLoss)+")\n")
