import pandas as pd 

df = pd.read_csv(r"C:\Users\rishi\output.csv")


print(df)
print(df.duplicated())