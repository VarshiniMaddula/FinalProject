import re
from collections import Counter

def analyze_mi_grades(file_path):
    # Read the content of the file using the appropriate encoding
    with open(file_path, 'r', encoding='utf-16') as file:
        content = file.readlines()

    # Regex pattern to capture grades following the specific format observed
    grade_pattern = re.compile(r' - ([A-F]) \(\d+\.\d+\)$')

    # Extract grades using the refined pattern
    grades = [grade_pattern.search(line).group(1) for line in content if grade_pattern.search(line)]

    # Count the frequency of each grade
    grade_counts = Counter(grades)

    # Print the frequencies
    for grade, count in grade_counts.items():
        print(f"Grade {grade}: {count}")

# Example usage of the function
file_path = 'C:/User/varshini/Downloads/FinalProject/Results/mi_results_spyder.txt'  
analyze_mi_grades(file_path)
