import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)

high_salery = df[df['Salary'] > 50000]
print('Employees with salery > 50000')
print(high_salery)

# filtering rows salery > 50k & age > 30
filtered = df[(df['Age'] > 19) & (df['Salary'] > 50000)]
print('Employee list Age > 30 + Salary > 50000')
print(filtered)

# using OR condition

filtered_or = df[(df['Age'] > 19) | (df["Performance Score"] > 80)]
print('Employees older than 20 OR performance score > 80')
print(filtered_or)
