import csv
import json
import pandas as pd
from functools import reduce

scores =  [72, 45, 88, 60, 91, 33, 78, 55]
grades = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C']
Student_records = [['Alice', 88], ['Bob', 72], ['Charlie', 45], ['David', 91], ['Eve', 78]]

##### Task 1: Sorting list from highest to lowest using a compact inline function approach (lambda)...

sorted_scores = sorted(scores, key=lambda x: x, reverse = True)
print(f"Sorted (high → low): {sorted_scores}")

##### Task 2: keeping only values that are 60 or above
valuesavobe59 = list(filter(lambda x: x >= 60, scores))
print(f"Passing scores (≥60): {valuesavobe59}")

##### Task 3: adding 5 bonus mark to all using map + lambda
adding_bonus_5 = list(map(lambda x: x + 5, scores))
print(f"Scores after +5 bonus: {adding_bonus_5}")


##### Task 4: Computing the total sum of all original scores.
total_sum = reduce(lambda x, y: x + y, scores)
print(f" Total of all scores: {total_sum}")


##### Task 5: Extracting all unique grade letters from the given list using set... As set contains uniques elements
unique_grade = set(grades)
print(f"Unique grades: {unique_grade}")


##### Task 6: Saving student records into a structured file named student_records.csv with two fields: name and score. Then reading it back and displaying each record.
df = pd.DataFrame(Student_records, columns=['name', 'score'])
df.to_csv('student_records.csv', index = False)
try:
    # df_read = pd.read_csv('student_records.csv')
    print("---marks.csv---")
    # print(df_read)
    with open('student_records.csv', 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:", e)

#### 7 , 8 both task here 💁‍♂️💁‍♂️💁‍♂️
##### Task 7 & 8: creating summary and writing it to a JSON file and reading back from that file
summary = {
    "total_students": len(scores),
    "highest_score": max(scores),
    "lowest_score": min(scores),
    "average_score": round(sum(scores) / len(scores), 2)
}

# writing to a json file
with open("summary.json", 'w') as f:
    json.dump(summary, f, indent=4)
#reading from json file
with open("summary.json", 'r') as f:
    datas = json.load(f)

print(json.dumps(datas, indent=4))