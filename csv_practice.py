import csv

with open('StdCANSheet.csv', 'r', newline='') as csvfile:
    read_value = csv.DictReader(csvfile)

    for row in read_value:
        print('Callback Function Name: {}'.format(row['MessageName']))
        print('Message ID: {}'.format(row['MessageID']))
        print('Pack Index: {}'.format(row['PackIndex']))