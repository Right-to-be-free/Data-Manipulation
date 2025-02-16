import pandas as pd 

df = pd.read_csv(r"C:\Users\rishi\Desktop\test.csv")

df['new_col'] = df['Age'].fillna(df['Age'].mean())
print(df['new_col'])
print(df)

df = df.drop(columns=['Age'])

df = df.rename(columns={'new_col':'Age'})
print(df)

df.insert(0, 'Age', df.pop('Age'))

print(df)

print(df.isnull().sum())