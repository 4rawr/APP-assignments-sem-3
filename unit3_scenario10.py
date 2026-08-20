import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Path to sports.csv")
args = parser.parse_args()

try:
    with open(args.filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        equipment_list = list(reader)
        
        print("All Equipment Records:")
        for item in equipment_list:
            print(item)
            
        search_id = input("\nEnter Equipment ID to search: ").strip()
        found = next((item for item in equipment_list if item.get("Equipment ID") == search_id), None)
        
        if found:
            print("Equipment Found:", found)
        else:
            print("Equipment not found.")
except FileNotFoundError:
    print("File not found.")
