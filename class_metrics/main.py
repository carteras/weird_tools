from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"

if __name__ == "__main__": 
    students_df = pd.read_csv( data / "absence_details_of_students.csv")
    my_df = students_df[students_df['Teacher Name'] == "Mr Adam Carter"]
    networking = my_df[(my_df['Unit Name'] == 'Yr 11/12 Networking/Security') | (my_df['Unit Name'] == 'Yr 11/12 Networking/Security A')]

    year_11s = networking[networking['School Year'] == "11"]['Student Name'].unique()
    year_12s = networking[networking['School Year'] == "12"]['Student Name'].unique()
    for i, name in enumerate(year_11s):
        print(i+1, 11, name)
    for i, name in enumerate(year_12s):
        print(i+1, 12, name)
    print(len(year_11s)/15, len(year_12s)/15)
