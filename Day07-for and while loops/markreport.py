# Student marks report
marks = {"Ram": 78, "Sita": 92, "Hari": 35, "Gita": 64}
total = 0

for name, mark in marks.items():
    if mark >= 40:
        print(f"{name}: {mark} Pass")
    else:
        print(f"{name}: {mark} Fail")
    total += mark

average = total / len(marks)
print("Class average:", average)