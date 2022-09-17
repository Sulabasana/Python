# import csv
# with open('rate.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     line_count = 0
#     for row in csv_reader:
#         addValue = row
        
#         print(row)
import pandas as pd

data = pd.read_csv('rate.csv')
# print(data)
# print(data.columns)
print(data.Rate)