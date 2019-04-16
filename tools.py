import csv
import os

def get_data():
    data =[]
    with open('./test_data/create_topic.csv') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            data.append(tuple(row))

    return data


print(get_data())
    