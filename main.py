import pandas as pd

csv_data = pd.read_csv('data/data.csv')
df = pd.DataFrame(csv_data)
print(df.head(5))

print(df.info())
print("Type:" , type(df['Employment']))

print(df[["Employment", "CodingActivities"]])
print(df['Q120'].value_counts())

pd_schema = pd.read_csv('data/schema.csv')