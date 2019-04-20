import csv
import os

def get_data(filePath=None):
    data =[]
    csv_file = os.path.join(rootPath(),'test_data/create_topic.csv')
    with open(csv_file) as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            data.append(tuple(row))

    return data


def rootPath():
    return os.path.dirname(os.path.abspath(__file__))

print(get_data())
    