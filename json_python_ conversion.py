import json

people_string = '''
{
    "people":[
        {
            "name": "John Smith",
            "phone": "123456789",
            "emails": ["johnsmith@compay.com", "johnsmith@home.com"],
            "has_license": false
        },
        {
            "name": "John Doe",
            "phone": "987654321",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# ^multi line string (looks like a python dictionary)
# key called "people"
# value of "people" is an array of more objects (2 more in this case)
# each object has a key of "name", "phone", "emails" and "has_license"
# this is a python string that happens to be valid json

# load this into a python object so that we can work with the data more easily

# to load this into python from a string we use json.loads (load S not loads)

data = json.loads(people_string)

print(data)  # prints a long bunched dictionary
print(type(data))  # <class 'dict'>

# now that we have a list (people) within a dictionary (data(people_string)) we can access certain parts

print(type(data["people"]))  # <class 'list'>

# for person in data["people"]:  # accessing people within data
#     #print(person)  # runs each person separately - they have also been converted into dictionaries
#     print(person["name"])  # will just print the name values

# now we have a python object we can edit we want to delete the phone number
for person in data["people"]:
    del person["phone"]

# to load this into JSON from a dictionary we use json.dumps (dump S not dumps)

new_string = json.dumps(data)
# new_string = json.dumps(data, indent = 2)  # indent states the number of indentations per item in the string
# new_string = json.dumps(data, indent = 2, sort_keys = True)  # sorts the keys alphabetically

print(new_string)  # prints out the JSON string but this time without the phone number








