import requests
import csv
from datetime import datetime 

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/banklist.csv'
response = requests.get(url)

with open("banklist.csv", "w") as localfile:
    localfile.write(response.text)

filtered_banks = []

with open("banklist.csv", "r") as localfile: 
    reader = csv.DictReader(localfile)
    for bank in reader:
        if bank["State\xa0"] == "CA":
            date_data = bank["Closing Date\xa0"]
            date_object = datetime.strptime(date_data, "%d-%b-%y")
            date_string = date_object.strftime("%Y-%m-%d")

            bank["Closing Date\xa0"] = date_string
            filtered_banks.append(bank)
            
col_headers = ["Bank Name\xa0", "City\xa0", "State\xa0", "Cert\xa0", "Acquiring Institution\xa0", "Closing Date\xa0", "Fund"]

with open("failed_banks_ca.csv", "w") as filteredfile:
    dict_writer = csv.DictWriter(filteredfile, fieldnames = col_headers)
    dict_writer.writeheader()
    dict_writer.writerows(filtered_banks)

bank_count = len(filtered_banks)
print("There are " + str(bank_count) + " failed banks in CA.")