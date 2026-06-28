import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Names (single column return series)")
name = df['Name']
print(name)

# Selecting multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and salary')
print(subset)