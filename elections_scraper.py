import requests
from bs4 import BeautifulSoup as bs
import sys
import csv

cities = {} # {city_number: [city_name, city_link, [registered, envelopes, valid], {political_parties}]}
political_parties = {}
csv_header = ["code", "location", "registered", "envelopes", "valid"]
url_district = sys.argv[1]
file_name = sys.argv[2]

#spouštění z Pycharmu:
#url_district = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202"
#file_name = "vysledky.csv"

def extract_soup():
    print(f"STAHUJI DATA Z VYBRANEHO URL: {url_district}")
    getr = requests.get(url_district)
    soup = bs(getr.text, "html.parser")
    cities_tables = soup.find_all("table")

    return cities_tables

def extract_cities():
    # tabulka měst
    for table in extract_soup():
        for row in table.find_all("tr"):
            if row.find("td", {"class": "overflow_name"}) is not None:
                city = []
                city_name = row.find("td", {"class": "overflow_name"}).text
                city_number = int(row.find("td", {"class": "cislo"}).text)
                city_link = url_district.rsplit('/', 1)[0] + "/" + row.find("a").get("href")
                city.append(city_name)
                city.append(city_link)
                cities[city_number] = city

def extract_city_data():
    for city in cities:
        url_city = cities[city][1]
        getr = requests.get(url_city)
        soup = bs(getr.text, "html.parser")
        city_tables = soup.find_all("table")
        city_results = {}

        # voliči v daném městě
        city_voters = city_tables[0]
        city_data = []
        registered = city_voters.find("td", {"headers": "sa2"}).text
        envelopes = city_voters.find("td", {"headers": "sa3"}).text
        valid = city_voters.find("td", {"headers": "sa6"}).text

        city_data.append(registered.replace(chr(160), ""))
        city_data.append(envelopes.replace(chr(160), ""))
        city_data.append(valid.replace(chr(160), ""))
        cities[city].append(city_data)

        # 1. tabulka výsledků voleb
        for row in city_tables[1].find_all("tr"):
            if row.find("td", {"class": "cislo"}, {"headers": "t1sa1 t1sb1"}) is not None:
                index = row.find("td", {"class": "cislo"}, {"headers": "t1sa1 t1sb1"}).text # číslo strany
                if index not in political_parties.keys():
                    political_parties[index] = row.find("td", {"headers": "t1sa1 t1sb2"}).text # název strany
                city_results[index] = (row.find("td", {"headers": "t1sa2 t1sb3"}).text).replace(chr(160), "") # hlasy v dané obci

        # 2. tabulka výsledků voleb
        for row in city_tables[2].find_all("tr"):
            if row.find("td", {"class": "cislo"}, {"headers": "t2sa1 t2sb1"}) is not None:
                index = row.find("td", {"class": "cislo"}, {"headers": "t2sa1 t2sb1"}).text # číslo strany
                if index not in political_parties.keys():
                    political_parties[index] = row.find("td", {"headers": "t2sa1 t2sb2"}).text # název strany
                city_results[index] = (row.find("td", {"headers": "t2sa2 t2sb3"}).text).replace(chr(160), "") # hlasy v dané obci

        cities[city].append(city_results)

def write_csv():
    print(f"UKLADAM DO SOUBORU: {file_name}")

    for party in political_parties:
        csv_header.append(political_parties[party])

    f = open(file_name, "w", encoding="utf-8", newline="")
    f_writer = csv.writer(f)
    f_writer.writerow(csv_header)
    rows = []

    for city in cities:
        row = []
        row.append(city)
        row.append(cities[city][0])

        for value in cities[city][2]:
            row.append(value)

        for key in cities[city][3]:
            row.append(cities[city][3][key])

        rows.append(row)
    f_writer.writerows(rows)

if __name__ == "__main__":
    extract_cities()
    extract_city_data()
    write_csv()
    print("UKONCUJI elections_scraper")