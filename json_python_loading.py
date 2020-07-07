import json

# load JSON files into Python objects
# write those objects back into JSON files
# json.load method (not loads)
# with open() statement will open a JSON file

with open("counties.json") as count:
    data = json.load(count)
