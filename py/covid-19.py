# ----------------------------- #
# COVID-19 Dashboard v1.0       #
# Copyright (c) 2021 miniprime1 #
#                               #
# Referenced: bit.ly/2Oi3Urq    #
# License: bit.ly/3b3qkFl       #
# Language: Python 3.7.8        #
# OS: Windows, MacOS, Linux     #
# ----------------------------- #

import requests
from pydantic import *

JOHN_HOPKINS = "john_hopkins"
SOURCES = [JOHN_HOPKINS]

def install_requirements():
    import sys, os
    os.system(sys.executable + " -m pip install pydantic")
    os.system(sys.executable + " -m pip install requests")

class CovidModel(BaseModel):
    id: str = Field(..., alias="OBJECTID")
    country: str = Field(..., alias="Country_Region")
    confirmed: int = Field(0, alias="Confirmed")
    active: int = Field(0, alias="Active")
    deaths: int = Field(0, alias="Deaths")
    recovered: int = Field(None, alias="Recovered")
    latitude: float = Field(None, alias="Lat")
    longitude: float = Field(None, alias="Long_")
    last_update: int = Field(0, alias="Last_Update")


class CountryModel(BaseModel):

    id: str = Field(..., alias="OBJECTID")
    name: str = Field(..., alias="Country_Region")

BASE_URL = "https://services1.arcgis.com"
PATH = ("/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/2/query")
URL = BASE_URL + PATH
SOURCE = JOHN_HOPKINS


class Covid:
    def __init__(self):
        self.source = SOURCE

    @staticmethod
    def __get_total_cases_by_country_id(object_id: str) -> dict:
        params = dict(
            f="json",
            where=f"OBJECTID = {object_id}",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            resultOffset="0",
            resultRecordCount="1",
            cacheHint="true",
        )
        response = requests.get(URL, params=params).json()
        try:
            return response["features"][0]["attributes"]
        except KeyError:
            raise Exception(response)

    def __get_total_by_case(self, case: str) -> int:
        params = dict(
            f="json",
            where="Confirmed > 0",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            outStatistics=str(
                [
                    {
                        "statisticType": "sum",
                        "onStatisticField": f"{case}",
                        "outStatisticFieldName": "value",
                    }
                ]
            ),
            cacheHint="true",
        )
        response = requests.get(URL, params=params).json()
        try:
            return response["features"][0]["attributes"]["value"]
        except KeyError:
            raise Exception(response)

    def __get_all_cases(self) -> list:
        params = dict(
            f="json",
            where="Confirmed > 0",
            returnGeometry="false",
            spatialRel="esriSpatialRelIntersects",
            outFields="*",
            orderByFields="Confirmed desc",
            resultOffset="0",
            resultRecordCount="200",
            cacheHint="true",
        )
        response = requests.get(URL, params=params).json()
        try:
            return response["features"]
        except KeyError:
            raise Exception(response)

    def get_data(self) -> list:
        cases = self.__get_all_cases()
        return [CovidModel(**case["attributes"]).dict() for case in cases]

    def get_total_active_cases(self) -> int:
        return self.__get_total_by_case("Active")

    def get_total_deaths(self) -> int:
        return self.__get_total_by_case("Deaths")

    def get_total_confirmed_cases(self) -> int:
        return self.__get_total_by_case("Confirmed")

    def get_total_recovered(self) -> int:
        return self.__get_total_by_case("Recovered")

    def list_countries(self) -> list:
        cases = self.__get_all_cases()
        return [CountryModel(**case["attributes"]).dict() for case in cases]

    def get_status_by_country_id(self, country_id) -> dict:
        case = self.__get_total_cases_by_country_id(country_id)
        return CovidModel(**case).dict()

    def get_status_by_country_name(self, country_name) -> dict:
        country = filter(
            lambda country: country["name"].lower() == country_name.lower(),
            self.list_countries(),
        )
        try:
            country = next(country)
        except StopIteration:
            raise ValueError(
                f"There is no country called '{country_name}', to check available country names use `list_countries()`"
            )
        case = self.__get_total_cases_by_country_id(country["id"])
        return CovidModel(**case).dict()

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