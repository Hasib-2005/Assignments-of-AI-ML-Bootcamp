import re
import json

##### Task 1: Creating diary.txt and storing entries

entries = [
    "2024-06-01: Had a great day at the park.",
    "2026-06-02: Finished reading a good book.",
    "2024-06-03: Cooked dinner for the family."
]

try:
    with open("diary.txt", "w") as f:
        for entry in entries:
            f.write(entry + "\n")
except Exception as e:
    print("Error:", e)


##### Task 2: Adding two more entries
try:
    with open("diary.txt", "a") as f:
        f.write("2024-06-04: Went for a long morning walk.\n")
        f.write("2024-06-05: Started learning about Python files.\n")

except Exception as e:
    print("Error:", e)

print("--- diary.txt ---")

with open("diary.txt", "r") as f:
    content = f.read()
    print(content)

##### Task 3: Extracting all dates

dates = re.findall(r"\d{4}-\d{2}-\d{2}", content)
print("Dates found:", dates)

##### Task 4: Searching words
if "book" in content:
    print(f'Searching for "{"book"}" → Found')
else:
    print(f'Searching for "{"book"}" → Not found')
if "movie" in content:
    print(f'Searching for "{"movie"}" → Found')
else:
    print(f'Searching for "{"movie"}" → Not found')


##### Task 5: Unique words longer than 4 characters

words = content.split()

unique_words = {
    word.strip(".,!?")
    for word in words
    if len(word.strip(".,!?")) > 4
}

print("Unique words:", unique_words)

##### Task 6: Opening a non-existing file

try:
    with open("unknown.txt", "r") as f:
        pass
except FileNotFoundError:
    print("Error: file not found")
finally:
    print("Diary access attempt complete.")

##### Task 7: Building Summary

entries_list = content.strip().split("\n")

summary = {
    "total_entries": len(entries_list),
    "dates": dates,
    "longest_entry": max(entries_list, key=len)
}


##### Task 8: Saving summary in a file and reading it back & printing
with open("summary.json", "w") as f:
    json.dump(summary, f, indent=4)

with open("summary.json", "r") as f:
    data = json.load(f)

print("{")
print(f' "total_entries": {data["total_entries"]},')
print(f' "dates": {json.dumps(data["dates"])},')
print(f' "longest_entry": "{data["longest_entry"]}"')
print("}")