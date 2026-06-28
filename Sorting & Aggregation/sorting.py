#sorting data
#SORTING DATA : COLUMN  sort_values()
# df.sort_values(bye="Column Name", True/False, inplace = True)

import pandas as pd

data = {
    "Name" : ['Kartik', 'Prashant', 'Yash'],
    "Age" : [19,20,23],
    "Salary" : [50000, 340000,70000]

}

df = pd.DataFrame(data)
df.sort_values(bye="Age",ascending=True, inplace = True)
print('Sorted Age by Descending')
print(df)