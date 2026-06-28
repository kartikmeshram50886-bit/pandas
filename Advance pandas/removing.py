import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance_Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)
print(df)

# df.drop(columns = ["Column_Name"], inplace = True)

print('Modified Data')
df.drop(columns = ["Performance_Score","Age"], inplace = True)
print(df)