from inspect import currentframe, getframeinfo
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
filename = getframeinfo(currentframe()).filename
here = Path(filename).resolve().parent
data = Path.cwd() / ".data"

lines = {}

subjects = []

rooms = {}
@dataclass
class Subject:
    subject: str
    code: str
    room: str
    teacher: str


class Room:
    def __init__(self, room, max_size, line):
        self.room = room
        self.max_size = max_size
        self.lines = []
        self.lines.append(line)

    def update_size(self, size):
        if size > self.max_size: self.max_size = size

    def get_lines(self):
        return set(self.lines)

def filter_codes(line):
    line = line.strip()
    subject, room, teacher = line.split(",")
    subject_code = subject[-10:]
    subject_name = subject[:-10]
    subject_code = subject_code[1:-1]
    return subject_name, subject_code, room, teacher

def filter_lines(path, df):
    with open(path) as line_descriptor:
        print(path)
        lines = line_descriptor.readlines()
        for line in lines:
            try:
                subject_name, subject_code, room, teacher = filter_codes(line)
            except: 
                print("-----------------------",line)
            students_in_subject = len(df[df['Unit Code'] == subject_code])
            line = subject_code[0]
            _, room = room.split(":")
            
            # print(subject_name, subject_code, room, teacher, students_in_subject)
            if room not in rooms:
                rooms[room] = Room(room, students_in_subject, line)
            else:
                rooms[room].lines.append(line)
                rooms[room].update_size(students_in_subject)
                
def get_spare_lines(lines):
    max_lines = ['1', '2','3','4','5','6','7']
    out = []
    for line in max_lines:
        if line not in lines:
            out.append(line)
    return out

def filter_all_lines(students_df):

    for i in range(1, 8):
        filter_lines(data / f"line.{i}", students_df)

def update_rooms_file(room, fd):
    lines = sorted(rooms[room].get_lines())
    spare_lines = get_spare_lines(lines)
    print(room.strip(), rooms[room].max_size, ",".join(spare_lines))
    fd.write(f"{room.strip()} {rooms[room].max_size} {','.join(spare_lines)}\n")

def main():
    students_df = pd.read_csv(data / "absence_details_of_students.csv")
    filter_all_lines(students_df)
    with open(here/'rooms', 'w') as fd:
        for room in rooms:
            if room.strip() in ["CCCARE","HeLP", "DANCE", "DRAMA", "GYM", "MUSIC"]: continue
            if len(rooms[room].get_lines()) < 7 and rooms[room].max_size > 15:
                update_rooms_file(room, fd)

if __name__ == "__main__":
    main()
