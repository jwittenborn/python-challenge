import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Candidates =[]
# uniqueCandidates =[ ]
# uniqueCandidateVotes =[ 0 ]

rowCounter=0

CandidateDict = {
}

# names = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvreader)

    for row in csvreader:
        rowCounter=rowCounter+1
        CandidateName = row[2]
        # names.append(CandidateName)
        if row[2] in CandidateDict:
            CandidateDict[CandidateName]=CandidateDict[CandidateName]+1
        else:
            CandidateDict[CandidateName] = 1


# print(rowCounter)
# print(CandidateDict)

# print(f'{John["name"]} is {John["age"]}' )
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {rowCounter}")
print("-------------------------")

for x, y in CandidateDict.items():
    # print(x, y)
    percentVote = float(y)/rowCounter*100
    print(f' {x}: {percentVote:.3f}% {y}')
    
print("-------------------------")


max_key = max(CandidateDict, key=CandidateDict.get)
print(f"Winner:  {max_key}")
print("-------------------------")
  
  

# KhanVotes = CandidateDict[0]
# print(KhanVotes)


# unique_names = set(names)

# for name in unique_names:

#     count = 0
#     for i in range(0, len(names)):
#         if names[i] == name:
#             count = count + 1
#     print(count)


# print(f"Total votes:  {str(rowCounter)}")

