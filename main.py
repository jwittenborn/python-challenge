
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

rowCounter=0
netProfitLoss = 0.0
monthlyChange =0.0
lastMonthProfitLoss = 0.0

MaxMonth = ""
MaxProfit = 0.0

MinMonth = ""
MinProfit = 0.0

monthlyChangeList = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #lastMonthProfitLoss = row[1]

    for row in csvreader:
        rowCounter=rowCounter+1
        netProfitLoss = netProfitLoss + float(row[1])

        if rowCounter>=2:
            monthlyChange = float(row[1]) - float(lastMonthProfitLoss)

            monthlyChangeList.append(monthlyChange)

            if monthlyChange > float(MaxProfit):
                MaxProfit = monthlyChange
                MaxMonth = row[0]

            if monthlyChange < float(MinProfit):
                MinProfit = monthlyChange
                MinMonth = row[0]

            
        
        lastMonthProfitLoss = row[1]


#avgChange = netProfitLoss / rowCounter

print(f"Total months:  {str(rowCounter)}")
print(f"Total:  ${str(netProfitLoss)}")



runningChange = 0.0

for change in monthlyChangeList:
    runningChange = runningChange + change
    # print(str(change))

avgChange = runningChange / (rowCounter-1)

print(f"Average change:  ${str(avgChange)}")
print(f"Greatest increase in profits: {MaxMonth} ( ${str(MaxProfit)})") 
print(f"Greatest decrease in profit: {MinMonth} ( ${str(MinProfit)})") 





output_path = os.path.join("Resources", "output.txt")

file = open(output_path, 'w') 

file.writelines(f"Total months:  {str(rowCounter)}\n")
file.writelines(f"Total:  ${str(netProfitLoss)}\n")
file.writelines(f"Average change:  ${str(avgChange)}\n")
file.writelines(f"Greatest increase in profits: {MaxMonth} ( ${str(MaxProfit)})\n")
file.writelines(f"Greatest decrease in profit: {MinMonth} ( ${str(MinProfit)})\n")
file.close() 

    #txtwriter.writerow(["Total Months: "  str(rowCounter)])