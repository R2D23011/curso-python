import csv
import json



def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = dict(iterable)
      data.append(country_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  formatted_data = json.dumps(data, indent=2)
  print(data[0])