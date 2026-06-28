# adding columns
import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df['Salary'] = 0.1
print(df)

# using insert
# df.insert(loc, "column_name", some_data)

# df.insert(0, "Employee ID", [10,20,30,40,50,60] )
# print(df)

# .loc[]
# df.loc[row_index, "Column Name"] = new_value

df.loc[0,'Salary'] = 55000
print(df)