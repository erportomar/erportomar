import pandas as pd
data_frame=pd.read_excel('jdahs.xlsx')
print(data_frame)
dict = {}
for position, Launguage in enumerate(data_frame["Launguage"]):
    Date = data_frame["Date"][position]
    dict[Launguage] = Date

print(dict)
