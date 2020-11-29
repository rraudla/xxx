import csv

with open('adsavalik-1697399122.csv') as csvfile1:
    readCSV = csv.DictReader(csvfile1, delimiter=";")
    print(readCSV)

    addresses_dict = {}

    for row in readCSV:
        row_splitted = row['AADRESS'].split(', ')

        if row_splitted[0] not in addresses_dict.keys():
            addresses_dict[row_splitted[0]] = {row_splitted[1]: [row_splitted[2]]}
        else:
            if row_splitted[1] not in addresses_dict[row_splitted[0]].keys():
                addresses_dict[row_splitted[0]][row_splitted[1]] = [row_splitted[2]]
            else:
                addresses_dict[row_splitted[0]][row_splitted[1]].append(row_splitted[2])
    try:
        filehandler = open('../addresses.csv', 'wt')
        filehandler.write(str(addresses_dict))
        filehandler.close()
    except:
        print('unable to write')




