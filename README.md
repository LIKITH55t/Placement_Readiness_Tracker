 Placement Readiness Tracker
Same data. Same questions. Two approaches: Pure Python and NumPy.

A beginner-friendly data analysis project that explores simulated student skill scores using pure Python and NumPy separately. The goal is to understand how lists and loops compare with array-based calculations.
Current Scope
Both implementations cover these four tasks:
1. Calculate the average Python score across the batch.
2. Find the highest and lowest Aptitude scores.
3. Count students with Communication scores strictly above 70.
4. Calculate the gap between each student's best and worst skill scores.
This version covers the initial numerical analysis only. Pandas analysis, readiness scoring, classification, charts, and the final report are not included yet.
Dataset
generate_placement_data.py creates placement_readiness.csv with 120 simulated students and eight columns.
Column	Description
Student_ID	Invented student identifier
Branch	CSE, ECE, IT, or MECH
Python_Score	Python score out of 100
SQL_Score	SQL score out of 100
Aptitude_Score	Aptitude score out of 100
Communication_Score	Communication score out of 100
Projects_Completed	Number of projects
Mock_Interviews_Attended	Number of mock interviews


All records are simulated for learning. They do not represent real students. Do not use real classmates' data for this exercise.
The generator has no fixed random seed, so running it again changes the data. Keep the same generated CSV when comparing both solutions.
Project Files
Keep these files together inside the Placement_Readiness_Tracker folder:
File	Purpose
generate_placement_data.py	Generates the simulated dataset
placement_readiness.csv	Shared input for both solutions
pure_python_solution.py	Analysis using CSV dictionaries, lists, loops, and built-in functions
numpy_solution.py	Analysis using NumPy arrays
README.md	Project overview and instructions


Requirements
- Python 3
- NumPy for the NumPy solution
The pure Python solution uses only standard-library modules: csv and pathlib. The generator also uses the standard-library random module.
How to Run
Open the project folder in VS Code and open its terminal. Run the following commands from that folder.
1. Install NumPy
python -m pip install numpy
2. Generate the dataset once
python generate_placement_data.py
Skip this step if you already have your generated CSV. The generator writes its output into the terminal's current folder.
3. Run the pure Python solution
python pure_python_solution.py
4. Run the NumPy solution
python numpy_solution.py
Both analysis scripts locate the CSV relative to their own file location using Path(__file__).parent.
Comparing the Approaches
Task	Pure Python	NumPy
Load scores	csv.DictReader, followed by integer conversion	np.loadtxt with dtype=int
Average Python score	sum(values) / len(values)	np.mean(scores[:, 0])
Highest Aptitude score	max(aptitude_scores)	np.max(scores[:, 2])
Lowest Aptitude score	min(aptitude_scores)	np.min(scores[:, 2])
Communication above 70	Loop, condition, and counter	np.sum(scores[:, 3] > 70)
Each student's skill gap	max(skill_scores) - min(skill_scores) inside a loop	np.max(scores, axis=1) - np.min(scores, axis=1)


Pure Python makes each processing step explicit. NumPy applies operations to entire arrays without writing a Python loop for each calculation. The NumPy version still uses a loop to print the student IDs and gaps.
No execution-time benchmark is included in this project.
Understanding the NumPy Array
The score array has shape (120, 4): one row per student and one column per skill.
Array column index	Skill
0	Python
1	SQL
2	Aptitude
3	Communication


- scores[:, 0] selects the Python score for every student.
- axis=1 works across skills within each student's row.
- axis=0 works down students within each skill column.
For example, if one student's scores are [80, 65, 75, 50], their skill gap is 80 - 50 = 30. This is an illustration, not a result from the generated dataset.
Checking the Results
Both scripts print their results in the terminal. For the same CSV, compare:
- The average Python score, rounded to two decimal places.
- The highest and lowest Aptitude scores.
- The count of Communication scores above 70; a score of exactly 70 is excluded.
- The skill gap for each matching Student ID.
The outputs should agree. Actual values depend on the generated CSV; no dataset-specific results are recorded here.
Troubleshooting
FileNotFoundError
Make sure placement_readiness.csv is in the same folder as both analysis scripts. If the generator saved it in the parent folder, move the existing CSV into the project folder.
ModuleNotFoundError: No module named 'numpy'
Install NumPy with python -m pip install numpy using the same Python environment that runs the script.
Learning Outcomes
- Read CSV data and convert text values into numbers.
- Use lists, loops, conditions, and built-in functions.
- Load and slice NumPy arrays.
- Use Boolean comparisons to count matching values.
- Understand row-wise calculations with axis=1.
- Compare two implementations using identical input data.
Question for Class
Why does calculating each student's skill gap require axis=1, and what would the result represent if we used axis=0 instead?