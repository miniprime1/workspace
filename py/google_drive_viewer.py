from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tabulate import tabulate
import pandas as pd

print("Google Drive Viewer v1.0")
print("Copyright (c) 2020 miniprime1\n")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

listed = drive.ListFile().GetList()
df = pd.DataFrame.from_dict(listed)
df = df[['title', 'id', 'modifiedByMeDate', 'mimeType']]
pd.options.display.max_columns = None
print(tabulate(df, headers="keys", tablefmt="psql"))