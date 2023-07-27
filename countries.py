import pandas as pd

data_frame=pd.read_excel('countries.xlsx')
print(data_frame)


dict={}

for position, name in enumerate(data_frame["NAME"]):
    country = data_frame["COUNTRY"][position]
    dict[name] = country

print(dict)
