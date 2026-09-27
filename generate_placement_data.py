import csv
import random

NUM_STUDENTS = 120
OUTPUT_FILE = "placement_readiness.csv"

random.seed()

BRANCHES = ["CSE", "ECE", "IT", "MECH"]

COLUMNS = [
    "Student_ID",
    "Branch",
    "Python_Score",
    "SQL_Score",
    "Aptitude_Score",
    "Communication_Score",
    "Projects_Completed",
    "Mock_Interviews_Attended",
]


def clamp(value, low=0, high=100):
    return max(low, min(high, int(round(value))))


def make_one_student(student_number):
    branch = random.choices(
        BRANCHES, weights=[40, 25, 25, 10]
    )[0]

    ability = random.gauss(60, 15)

    if branch in ("CSE", "IT"):
        tech_bonus = random.uniform(4, 12)
    else:
        tech_bonus = random.uniform(-6, 4)

    python_score = clamp(
        ability + tech_bonus + random.gauss(0, 10)
    )
    sql_score = clamp(
        ability + tech_bonus * 0.6 + random.gauss(0, 12)
    )
    aptitude_score = clamp(
        ability + random.gauss(0, 12)
    )
    communication_score = clamp(
        ability - 12 + random.gauss(0, 14)
    )

    projects = clamp(
        random.gauss(ability / 22, 1.2), low=0, high=8
    )
    mocks = clamp(
        random.gauss(ability / 18, 1.8), low=0, high=12
    )

    return [
        f"S{student_number:04d}",
        branch,
        python_score,
        sql_score,
        aptitude_score,
        communication_score,
        projects,
        mocks,
    ]


def main():
    rows = []

    for i in range(1, NUM_STUDENTS + 1):
        rows.append(make_one_student(i))

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(rows)

    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")
    print("This is simulated data, not real student data.")


if __name__ == "__main__":
    main()