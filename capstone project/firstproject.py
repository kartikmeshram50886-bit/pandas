import numpy as np
import pandas as pd

df = pd.read_excel("pandas/Employar salary sheet.xlsx")
print(df)

print('Display first 10 line ')
print(df.head())

print(df.info())
print('Displaying the data of info')
print(df)


#selecting the data
subset = [["Salary","Age","Name"]]
print(subset)

# adding the data

# df = pd.DataFrame(data)
# print(df)

df.loc[0,"Salary"] = 50000
print(df)

print("Modified_data")
df.drop(columns = ["Performance"],inplace = True)
print(df)

# missing value find out
print(df.isnull())

df["Salary"].max()
print(df)

df['Age'].fillna(df['Age'].mean(), inplace = True)
df['Salary'].fillna(df['Salary'].mean(), inplace = True)
print(df)

filtered_or = df[(df['Age'] > 19) | (df["Salary"] >= 80000)]
print(' Employar older than 21  OR  salary is >= 80000')
print(filtered_or)

