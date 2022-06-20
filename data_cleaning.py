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

df.to_csv("Meters_mod.csv", index=False)