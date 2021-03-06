from urllib import request
from bs4 import BeautifulSoup

print("Weather Live v1.0")
print("Copyright (c) 2020 miniprime1")
print("[Region: Republic of Korea]\n")

target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()