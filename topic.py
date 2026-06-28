"""
1- how big is your data
2- what are the names of columns

shape and coloumns
"""

import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash', 'Vaibhav','Lucky', 'Pranay'],
    "Age" : [19,20,23,22,18,24],
    "Salary" : [50000, 340000,70000,100000,200000,400000],
    "Performance Score" : [78,98,79,98,89,80]

}

df = pd.DataFrame(data)
print(df)

print(f'shape: {df.shape}')
print(f'Column Names: {df.columns}')

"""
(1000,20)
(5,4)
"""