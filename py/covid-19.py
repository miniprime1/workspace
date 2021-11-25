# Name: COVID-19 Dashboard v1.0       
# Referenc: bit.ly/2Oi3Urq    
# License: bit.ly/3b3qkFl       
# Language: Python 3.7.8        
# OS: Windows, MacOS, Linux 

import requests
from bs4 import BeautifulSoup
from pydantic import *
from decimal import *

WORLDOMETERS = "worldometers"
SOURCE = WORLDOMETERS
URL = "https://www.worldometers.info/coronavirus/"

def install_requirements():
    import sys, os
    for i in ["pydantic", "requests", "beautifulsoup4"]:
        os.system(f"{sys.executable} -m pip install {i}")

class CovidModel(BaseModel):
    country: str = Field(..., alias="Country,Other")
    total_cases: int = Field(0, alias="TotalCases")
    confirmed: int = Field(0, alias="TotalCases")
    new_cases: int = Field(0, alias="NewCases")
    deaths: int = Field(0, alias="TotalDeaths")
    new_deaths: int = Field(0, alias="NewDeaths")
    recovered: int = Field(0, alias="TotalRecovered")
    active: int = Field(0, alias="ActiveCases")
    active_cases: int = Field(0, alias="ActiveCases")
    critical: int = Field(0, alias="Serious,Critical")
    total_tests: int = Field(0, alias="TotalTests")
    total_tests_per_million: Decimal = Field(Decimal(0), alias="Tests/1M pop")
    total_cases_per_million: Decimal = Field(Decimal(0), alias="TotCases/1M pop")
    total_deaths_per_million: Decimal = Field(Decimal(0), alias="Deaths/1M pop")
    population: Decimal = Field(Decimal(0), alias="Population")

class Covid:
    def __init__(self):
        self.__url = URL
        self.__data = {}
        self.__fetch()
        self.__set_data()
        self.source = SOURCE

    def __fetch(self):
        response = requests.get(self.__url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "main_table_countries"})
        headers = table.find_all("th")
        self.__headers = [header.text.replace("\xa0", "") for header in headers]
        self.__rows = table.tbody.find_all("tr")
        self.__total_cases = soup.find_all("div", attrs={"class": "maincounter-number"})

    def __set_data(self):
        countries = ([attr.text.strip() for attr in row if attr != "\n"] for row in self.__rows)
        self.__data = {country[1].lower(): country for country in countries}

    def __format(self, _list: list) -> list:
        _list = [val.strip().replace(",", "") for val in _list]
        return [val if val and val != "N/A" else 0 for val in _list]

    def get_data(self) -> list:
        return [CovidModel(**dict(zip(self.__headers, self.__format(val)))).dict() for val in self.__data.values()]

    def get_status_by_country_name(self, country_name: str) -> dict:
        try: country_data = dict(zip(self.__headers, self.__format(self.__data[country_name.lower()]),))
        except KeyError: raise ValueError( f"There is no country called '{country_name}', to check available country names use `list_countries()`")
        return CovidModel(**country_data).dict()

    def list_countries(self) -> list:
        return list(self.__data.keys())

    @staticmethod
    def __to_num(string: str) -> int:
        return int(string.strip().replace(",", ""))

    def get_total_confirmed_cases(self) -> int:
        return self.__to_num(self.__total_cases[0].span.text)

    def get_total_deaths(self) -> int:
        return self.__to_num(self.__total_cases[1].span.text)

    def get_total_recovered(self) -> int:
        return self.__to_num(self.__total_cases[2].span.text)

    def get_total_active_cases(self) -> int:
        confirmed = self.get_total_confirmed_cases()
        deaths = self.get_total_deaths()
        recovered = self.get_total_recovered()
        return confirmed - (recovered + deaths)

if __name__ == '__main__':
    confirmed = Covid().get_total_confirmed_cases()
    deaths = Covid().get_total_deaths()
    recovered = Covid().get_total_recovered()

    print("COVID-19 Dashboard v1.0")
    print("Copyright (c) 2020 miniprime1\n")

    print("[Worldwide]")
    print("Confirmed:", confirmed)
    print("Deaths:", deaths)
    print("Recovered:", recovered)