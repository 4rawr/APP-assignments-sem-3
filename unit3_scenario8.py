import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Path to courses.csv")
args = parser.parse_args()

try:
    with open(args.filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        courses = list(reader)
        
        print("All Courses:")
        for course in courses:
            print(course)
            
        search_id = input("\nEnter Course ID to search: ").strip()
        found = next((c for c in courses if c.get("Course ID") == search_id), None)
        
        if found:
            print("Course Found:", found)
        else:
            print("Course not found.")
except FileNotFoundError:
    print("File not found.")
