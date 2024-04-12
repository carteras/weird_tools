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
    student_ids = my_df['Student Key'].unique()
    
    with open(data / 'students.add', 'w') as fd:
        for student_id in student_ids:
            # roll_group = my_df[my_df['Student Key'] == student_id]['Roll Group'].unique()[0]
            t_student = f"t{student_id:0>7}"
            foo = f"- name: {t_student}\n  groups: ['dialout']\n  password: \"{{ '{t_student}-password'}}\"\n"
            fd.write(foo)
    with open(data / 'students.passwords', 'w') as fd:
        for student_id in student_ids:
            # roll_group = my_df[my_df['Student Key'] == student_id]['Roll Group'].unique()[0]
            t_student = f"t{student_id:0>7}"
            foo = f"- name: {t_student}\n  password: {t_student}-password\n"
            fd.write(foo)
   
   
    #      name: 
    # groups: ["dialout"]
    # password: "{{ 'XXXX-password' | password_hash('sha512') }}"
    # print(f"liststudent_ids:0>7}")
    # for idx, row in my_df.iterrows():
    #     print(row['Student Key'], row['Student Name'])

    """Index(['Student ID', 'Student Key', 'Student Name', 'Teacher Name',
       'School Year', 'Roll Group', 'Unit Name', 'Unit Code',
       'Attended Percentage', 'Explained Absences Percentage',
       'Unexplained Absences Percentage', 'Attendance Requirement Percentage'],
      dtype='object')
    """