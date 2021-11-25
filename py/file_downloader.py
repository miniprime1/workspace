import urllib.request

print("File Downloader v1.0")
print("Copyright (c) 2020 miniprime1\n")

url = input("Enter URL: ")
path = input("Enter Save Path: ")
print('\nDownloading...')

try:
    urllib.request.urlretrieve(url, path)
    print("Done!")
    print("\nFile downloaded succesfully at", path)
except Exception as e:
    print("\nError!")
    print(str(e))

# For Test
# URL: http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg
# Path: /cat.png