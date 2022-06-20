from numpy import sign
import pandas as pd
import glob
import os

#Merging Meter A,B,C CSV Files into one file
joined_files = os.path.join("Dataset CSV File", "Meter*_mod.csv")

joined_list = glob.glob(joined_files)

df = pd.concat(
    map(pd.read_csv, joined_list), ignore_index=True)
print(df)

#Deleting extra columns
data = pd.read_csv("Meters_mod.csv")

data.drop('Speed of Sound1', inplace=True, axis=1)
data.drop('Speed of Sound2', inplace=True, axis=1)
data.drop('Speed of Sound3', inplace=True, axis=1)
data.drop('Speed of Sound4', inplace=True, axis=1)
data.drop('Speed of Sound5', inplace=True, axis=1)
data.drop('Speed of Sound6', inplace=True, axis=1)
data.drop('Speed of Sound7', inplace=True, axis=1)
data.drop('Speed of Sound8', inplace=True, axis=1)

print(data)



df.to_csv("Meters_mod.csv", index=False)