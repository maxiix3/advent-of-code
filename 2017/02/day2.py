import pandas as pd

data = pd.read_csv("./day2_puzzle.txt", sep='\t', header=None)
print("day2_1: " + str(sum(data.max(axis=1) - data.min(axis=1))))

summer = 0
for row in data.itertuples():
    for i in range(1,len(row)):
        for j in range(1,len(row)):
            if i != j and (row[i] % row[j] == 0):
                summer += row[i]/row[j]
print("day2_2: " + str(int(summer)))
