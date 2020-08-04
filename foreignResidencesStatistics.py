import pandas as pd
data = pd.read_table("/Users/hong/Downloads/report.txt", sep = "\t")
print(data.columns)
pd.series.