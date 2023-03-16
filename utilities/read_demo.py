""" This file will be deleted. Not part of the framework
To understand - how to read csv, excel, json """
import pandas

df = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")

print(df)
print(df.values.tolist())
print("-" * 100)

print(df.loc[0])

print(df.loc[0].tolist())
print(list(df.loc[0]))
print(tuple(df.loc[0]))

print(df.loc[0].tolist())
print(df.loc[1].tolist())

print(df.index)
print(60 * "-")

"""rows to be converted into list of list or list of tuple"""
# print(df.values)
# print(df.values.tolist())


# print(df.loc[0].tolist())
# print(df.loc[1].tolist())
#
# list=[df.loc[0].tolist(),df.loc[1].tolist()]
# print(list)
list = []
for i in df.index:
    print(df.loc[i].tolist())
    list.append(df.loc[i].tolist())

print(list)

list = []
for i in df.index:
    print(tuple(df.loc[i]))
    list.append(tuple(df.loc[i]))

print(list)

print(df.values)
print(df.values.tolist())

print("-" * 100)
"""Read excel and get as dataframe"""

df=pandas.read_excel(io="../test_data/orange_test_data.xlsx", sheet_name="test_add_valid_employee")
print(df)

print(df.values.tolist())

# print(df.loc[0].tolist())

"""To read using column name """

print(df.get(["User Name"]))

print("-" * 100)
print("-" * 100)
print("-" * 100)
"""Read Json File"""
dic=pandas.read_json(path_or_buf="../test_data/data.json",typ="dictionary")
print(dic)
print(dic['browser'])
print(dic['url'])
# print(dic['test_valid_data'])
