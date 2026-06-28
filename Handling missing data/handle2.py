# fillna()
# fillnalvalue,inplace = True
import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)
print(df)

# df.fillna(0, inplace = True)
df['Age'].fillna(df['Age'].mean(), inplace = True)
df['Salary'].fillna(df['Salary'].mean(), inplace = True)
print(df)
                

