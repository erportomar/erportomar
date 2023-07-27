import pandas as pd
#readin excel file
data_frame=pd.read_excel('countries_2.xlsx')
print(data_frame)


dict={}
#list!!!!
for position, name in enumerate(data_frame["Name"]):
    lastname = data_frame["Last Name"][position]
    country = data_frame["Country"][position]
    capital = data_frame["Capital"][position]
    launguage = data_frame["Launguage"][position]
    dict[name] = launguage

print(dict)