def get_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "Fail"

marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}

for name, mark in marks.items():
    print(name, mark, get_grade(mark))
