from pathlib import Path
import numpy as np

file_path = Path(__file__).parent / "placement_readiness.csv"

scores = np.loadtxt(
    file_path,
    delimiter=",",
    skiprows=1,
    usecols=(2, 3, 4, 5),
    dtype=int
)

average_python = np.mean(scores[:, 0])

print("Average Python score:", round(average_python, 2))
aptitude_scores = scores[:, 2]

highest_aptitude = np.max(aptitude_scores)
lowest_aptitude = np.min(aptitude_scores)

print("Highest Aptitude score:", highest_aptitude)
print("Lowest Aptitude score:", lowest_aptitude)
communication_scores = scores[:, 3]

communication_count = np.sum(communication_scores > 70)

print("Students with Communication above 70:", communication_count)
best_scores = np.max(scores, axis=1)
worst_scores = np.min(scores, axis=1)

skill_gaps = best_scores - worst_scores

student_ids = np.loadtxt(
    file_path,
    delimiter=",",
    skiprows=1,
    usecols=0,
    dtype=str
)

print("\nSkill gap for each student:")

for student_id, gap in zip(student_ids, skill_gaps):
    print(student_id, "Skill gap:", gap)