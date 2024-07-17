
from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from dataclasses import dataclass
from statistics import mean, median, mode


filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"

@dataclass
class Unit:
    course: str
    year: str
    unit: str
    unit_value: float
    unit_score: float
    grade: str

class Student:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
        self.units = []

    def add_unit(self, course, year, unit, unit_value, unit_score, grade):
        unit = Unit(course=course, year=year, unit=unit, unit_value=unit_value, unit_score=unit_score, grade=grade)
        self.units.append(unit)

    def list_units(self):
        return "".join(self.units)


def populate_students(student_ids, students_df):
    out = {}

    for id in student_ids:
        # student = it_students[it_students['StudentId1'] == id]
        student = students_df[students_df['StudentId1'] == id]
        # print(student['Fullname1'].iloc[0], student['CoursewithOtherSchool1'], student['UnitwithOtherCheck1'])
        
        for idx, row in student.iterrows():
            student_id = row['StudentId1']
            if student_id not in out:
                out[student_id] = Student(id = student_id, name = row['Fullname1'])
            
            if row['CoursewithOtherSchool1'] == "COLLEGE-BASED (ALLC)": continue
            if row['UnitwithOtherCheck1'].endswith("Non-ACT "): continue

            if row['longgrade1'] == "Pass": continue

            out[student_id].add_unit(
                course=row['CoursewithOtherSchool1'], 
                year=row['Year1'],
                unit=row['UnitwithOtherCheck1'],
                unit_value=row['UnitValue1'],
                unit_score = row['ScaledUnitScore1'],
                grade=row['longgrade1']
            )
    return out

if __name__ == "__main__":
    acs_students = "ALL_acs-Student Reports-Academic Record.2024.S1.csv"#@param {type: "string"}
    filtered_list = ['DIGITAL TECHNOLOGIES ', 'NETWORKING AND SECURITY ', 'ENGINEERING STUDIES ']
    # filtered_list = ['NETWORKING AND SECURITY ']
    acs_data = data / acs_students
    students_df = pd.read_csv(acs_data, converters={'StudentId1': '{:0>7}'.format})
    it_students = students_df[students_df['CoursewithOtherSchool1'].isin(filtered_list)]
    student_ids = it_students['StudentId1'].unique()

    students = populate_students(student_ids=student_ids, students_df=students_df)

    for student in students:
        scores = []
        tmp = []
        it = []
        for unit in students[student].units:
            scores.append(unit.unit_score)
            if unit.course in filtered_list: 
                tmp.append(f"{unit.unit:<44} {unit.unit_score}")
                it.append(unit.unit_score)
        if median(scores) == 0.00: continue
        print(f"{student}, {students[student].name:<35} {min(scores):<6,.2f} {max(scores):<6,.2f} {mean(scores):<6,.2f} {median(scores):<6,.2f}")
        # print("\n".join(tmp))
        print(f"IT: {min(it):>46,.2f} {max(it):<6,.2f} {mean(it):<6,.2f} {median(it):<6,.2f}")
        print('----')
    
