from pathlib import Path
from nozomi import api

print("Nozomi Downloader v1.0")
print("Copyright (c) 2021 miniprime1")
print("[Enter Ctrl+C to Exit]\n")

tptag = input("Enter Tag: ")
dltag = []

for i in range(2): dltag.append(tptag)

print("\nDownloading...")
try:
    for post in api.get_posts(dltag):
        api.download_media(post, Path.cwd())
except KeyboardInterrupt:
    print("Done!")
except Exception as e:
    print(str(e))