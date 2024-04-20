from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"
absences = data / "absence_details_of_students.csv"
students = pd.read_csv(absences)

excluded_units = [
    "613XMARS1",
    "513XCAOS1",
    "213XEAPS1",
    "742XCAQS1",
    "54BEAPS1",
    "24BMAPS1",
    "442XWAQS1",
    "64BBAZS1",
]

class Teacher:
    def __init__(self, name):
        self.name = name
        self.lines = {
        }
        self.codes = []
        self.total_size = 0
        self.is_connect_teacher = False
    
    def add_line(self, code, size):
        line = int(code[0])
        if line == 8: 
            self.is_connect_teacher = True
            return
        if code in excluded_units: return
        self.codes.append((code, size))
        # print(f"{line not in self.lines}, {line}")
        if line not in self.lines:
            self.lines[line] = size
        else: 
            self.lines[line] += size
        
        self.total_size += size

    def get_student_ratio(self):
        try: 
            return self.total_size/len(self.lines)
        except: 
            return 0
    
    def number_of_lines(self):
        return len(self.lines)



teachers = students['Teacher Name'].unique()
teachers_data = []
for teacher in teachers:
    section = students[students['Teacher Name'] == teacher]
    units = section['Unit Code'].unique()
    t = Teacher(teacher)
    total = 0
    for unit in units:
        unit_size = len(section[section['Unit Code'] == unit])
        total += unit_size
        t.add_line(unit, unit_size)
    teachers_data.append(t)

five_line_teachers = 0
total_teachers = len(teachers_data)
# teachers_data.sort(key=lambda t: len(t.lines), reverse=True)
teachers_data.sort(key=lambda t: (-len(t.lines), t.get_student_ratio()))

for t in teachers_data:
    if t.number_of_lines() == 5: five_line_teachers += 1
    if len(t.lines) > 0: print(t.name, len(t.lines), t.total_size, t.get_student_ratio(), t.codes)#, len(t.codes)/len(t.lines), t.codes)

print("five line teachers", five_line_teachers, total_teachers)

    