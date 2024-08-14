from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"


if __name__ == "__main__": 
    acs_courses = ["NETWORKING AND SECURITY ", "ENGINEERING STUDIES " ]
    students_df = pd.read_csv( data / "summary_of_student_absences 2024S2T3.csv", converters={'Student ID': '{:0>7}'.format})
    acs_df = pd.read_csv(data / "acs-Student Reports-Academic Record2024S2T3.csv", converters={'StudentId1': '{:0>7}'.format})
    my_df = students_df[students_df['Teacher'] == "Mr Adam Carter"]
    
    # print(my_df.head())
    networking = my_df[(my_df['Unit Name'] == 'Yr 11/12 Networking/Security') | (my_df['Unit Name'] == 'Yr 11/12 Networking/Security A')]

    engineering = my_df[(my_df['Unit Name'] == "Yr 11/12 Engineering Studies")]

    year_11s = networking[networking['Year'] == "11"][['Student Name', 'Student ID', "Unit Code", "Unit Name"]].drop_duplicates().sort_values(by='Unit Code')
    year_12s = networking[networking['Year'] == "12"][['Student Name', 'Student ID', "Unit Code", "Unit Name"]].drop_duplicates().sort_values(by='Unit Code')


    print("")



    for i, (name, student_id, unit_name, unit_code) in enumerate(year_11s.values):
        student_acs = acs_df[acs_df['StudentId1'] == student_id]
        # Filter the DataFrame based on the condition
        filtered_students = student_acs[student_acs['CoursewithOtherSchool1'].isin(acs_courses)]
        unit_types = []
        # Print the 'Uni   tAccredType1' fields for the filtered students
        for unit_type in filtered_students['UnitAccredType1']:
            # print(unit_type)
            unit_types.append(unit_type)

        if student_acs['IntendsT1'].unique().item() == "No" or 'T' not in unit_types:
            print(f"11 {name:<30} {student_id}\n\t {unit_name} {unit_code} should be in Accredited Cloud and Distributed Systems. \n\n\n")
            # print(i+1, 11, name, student_id, unit_name, unit_code, " | ",student_acs['IntendsT1'].unique().item(), " ".join(unit_types))

    for i, (name, student_id, unit_name, unit_code) in enumerate(year_12s.values):
        student_acs = acs_df[acs_df['StudentId1'] == student_id]
        # Filter the DataFrame based on the condition
        filtered_students = student_acs[student_acs['CoursewithOtherSchool1'].isin(acs_courses)]
        unit_types = []
        # Print the 'Uni   tAccredType1' fields for the filtered students
        for unit_type in filtered_students['UnitAccredType1']:
            # print(unit_type)
            unit_types.append(unit_type)

        if student_acs['IntendsT1'].unique().item() == "No" or 'T' not in unit_types:
            print(f"12 {name:<30} {student_id}\n\t {unit_name} {unit_code} should be in Accredited Cloud and Distributed Systems.  \n\n\n")

    # print(len(year_11s), len(year_12s))

    year_11s = engineering[engineering['Year'] == "11"][['Student Name', 'Student ID', "Unit Code", "Unit Name"]].drop_duplicates().sort_values(by='Unit Code')
    year_12s = engineering[engineering['Year'] == "12"][['Student Name', 'Student ID', "Unit Code", "Unit Name"]].drop_duplicates().sort_values(by='Unit Code')

    # "Yr 11/12 Engineering Studies",

    for i, (name, student_id, unit_name, unit_code) in enumerate(year_11s.values):
        student_acs = acs_df[acs_df['StudentId1'] == student_id]
        # Filter the DataFrame based on the condition
        filtered_students = student_acs[student_acs['CoursewithOtherSchool1'].isin(acs_courses)]
        unit_types = []
        # Print the 'Uni   tAccredType1' fields for the filtered students
        for unit_type in filtered_students['UnitAccredType1']:
            # print(unit_type)
            unit_types.append(unit_type)

        if student_acs['IntendsT1'].unique().item() == "No" or 'T' not in unit_types:
            print(f"11 {name:<30} {student_id}\n\t {unit_name} {unit_code} should be in Accredited Future Challenges & Innovations. \n\n\n")
            # print(i+1, 11, name, student_id, unit_name, unit_code, " | ",student_acs['IntendsT1'].unique().item(), " ".join(unit_types))

    for i, (name, student_id, unit_name, unit_code) in enumerate(year_12s.values):
        student_acs = acs_df[acs_df['StudentId1'] == student_id]
        # Filter the DataFrame based on the condition
        filtered_students = student_acs[student_acs['CoursewithOtherSchool1'].isin(acs_courses)]
        unit_types = []
        # Print the 'Uni   tAccredType1' fields for the filtered students
        for unit_type in filtered_students['UnitAccredType1']:
            # print(unit_type)
            unit_types.append(unit_type)

        if student_acs['IntendsT1'].unique().item() == "No" or 'T' not in unit_types:
            print(f"12 {name:<30} {student_id}\n\t {unit_name} {unit_code} should be in Accredited Future Challenges & Innovations.  \n\n\n")
