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
    for banks in reader:
        if banks["State\xa0"] == "CA":
            date_data = banks["Closing Date\xa0"]
            date_object = datetime.strptime(date_data, "%d-%b-%y")
            date_string = date_object.strftime("%Y-%m-%d")

            for date in banks:
                banks["Closing Date\xa0"] = date_string
            filtered_banks.append(banks)
            
col_headers = ["Bank Name\xa0", "City\xa0", "State\xa0", "Cert\xa0", "Acquiring Institution\xa0", "Closing Date\xa0", "Fund"]

with open("failed_banks_ca.csv", "w") as filteredfile:
    dict_writer = csv.DictWriter(filteredfile, fieldnames = col_headers)
    dict_writer.writeheader()
    dict_writer.writerows(filtered_banks)

x = len(filtered_banks)
print("There are " + str(x) + " failed banks in CA.")