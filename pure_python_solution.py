import csv
from pathlib import Path

file_path = Path(__file__).parent / "placement_readiness.csv"

students = []

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

print("Number of students:", len(students))
print("First student:", students[0])
python_scores = []

for student in students:
    score = int(student["Python_Score"])
    python_scores.append(score)

average_python = sum(python_scores) / len(python_scores)

print("Average Python score:", round(average_python, 2))
aptitude_scores = []

for student in students:
    score = int(student["Aptitude_Score"])
    aptitude_scores.append(score)

highest_aptitude = max(aptitude_scores)
lowest_aptitude = min(aptitude_scores)

print("Highest Aptitude score:", highest_aptitude)
print("Lowest Aptitude score:", lowest_aptitude)
communication_count = 0

for student in students:
    score = int(student["Communication_Score"])

    if score > 70:
        communication_count += 1

print("Students with Communication above 70:", communication_count)
print("\nSkill gap for each student:")

for student in students:
    skill_scores = [
        int(student["Python_Score"]),
        int(student["SQL_Score"]),
        int(student["Aptitude_Score"]),
        int(student["Communication_Score"])
    ]

    best_score = max(skill_scores)
    worst_score = min(skill_scores)
    gap = best_score - worst_score

    print(student["Student_ID"], "Skill gap:", gap)