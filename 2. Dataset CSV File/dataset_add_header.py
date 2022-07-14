from numpy import sign
import pandas as pd

# file to load data and add header 

# initiate empty array to store feature name
flow_velocity1 = []
flow_velocity2 = []
speed_sound1 = []
speed_sound2 = []
signal_strength2 = []
signal_quality2 = []
turbulence2 = []
transit_time2 = []
gain1 = []
gainA = []

# store feature name in the array
for i in range(8):
    flow_velocity1.append("Flow Velocity" + str(i + 1))
    speed_sound1.append("Speed of Sound" + str(i + 1))
    gain1.append("Gain" + str(i + 1))
    gainA.append("GainA" + str(i + 1))
    signal_strength2.append("Signal Strength" + str(i + 1))
    signal_quality2.append("Signal Quality" + str(i + 1))
    transit_time2.append("Transit time" + str(i + 1))

for i in range(4):
    flow_velocity2.append("Flow Velocity" + str(i + 1))
    speed_sound2.append("Speed of Sound" + str(i + 1))
    turbulence2.append("Turbulence" + str(i + 1))

# Meter A dataframe
df1 = pd.read_csv(
    "Meter A",
    sep="	",
    header=None,
    names=[
        "Flatness ratio",
        "Symmetry",
        "Crossflow",
        *flow_velocity1,
        *speed_sound1,
        "Average speed of sound",
        *gain1,
        *gainA,
        "Class Attruibute",
    ],
)

# Meter B dataframe
df2 = pd.read_csv(
    "Meter B",
    sep="	",
    header=None,
    names=[
        "Profile factor",
        "Symmetry",
        "Crossflow",
        "Swirl Angle",
        *flow_velocity2,
        "Average flow velocity",
        *speed_sound2,
        "Average speed of sound",
        *signal_strength2,
        *turbulence2,
        "Meter performance",
        *signal_quality2,
        *gain1,
        *transit_time2,
        "Class Attruibute",
    ],
)

# Meter C dataframe
df3 = pd.read_csv(
    "Meter C",
    sep="	",
    header=None,
    names=[
        "Profile factor",
        "Symmetry",
        "Crossflow",
        *flow_velocity2,
        *speed_sound2,
        *signal_strength2,
        *signal_quality2,
        *gain1,
        *transit_time2,
        "Class Attruibute",
    ],
)

# display DataFrame
# print(df1)
# print(df2)
# print(df3)

df1.to_csv("MeterA_mod.csv", index=False)
df2.to_csv("MeterB_mod.csv", index=False)
df3.to_csv("MeterC_mod.csv", index=False)
