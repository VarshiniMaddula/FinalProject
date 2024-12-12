import re
from collections import Counter

results_file_path = "C:/User/varshini/Downloads/FinalProject/Results/cc_results_spyder.txt"
# Read the content again using UTF-16 encoding
with open(results_file_path, 'r', encoding='utf-16') as file:
    cc_content = file.readlines()

# Regex to find grades in the text
grade_pattern = re.compile(r'\b[A-F]\b \(\d+\)')

# Extract grades
grades = [grade_pattern.search(line).group()[0] for line in cc_content if grade_pattern.search(line)]

# Count the frequency of each grade
grade_counts = Counter(grades)

# Save the results to a new text file
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count}\n")
