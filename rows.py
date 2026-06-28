# head() tall () # display 5 upper row, display 5 lower row
# head(n) display
# tail(n)  disply

import pandas as pd
df = pd.read_excel("pandas/Any year one-month calendar1.xlsx")

print('Display first 10 rows')
print(df.head())

print('Display last 10 row')
print(df.tail())