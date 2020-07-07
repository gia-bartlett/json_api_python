JSON:  

Again, huge thanks to Corey Schafer!  
https://www.youtube.com/watch?v=9N6a-VLBa2I   
JavaScript Object Notation  

- Originally inspired by JavaScript but now a language in it's own right  
- Very common data format for storing information  
- Used a lot when fetching data from online APIs  
- Also used for configuration files and different kinds of data that can be saved on your local machine  

no need to install - just import json

Convert JSON into Python:  

json.loads()

```python
import json

# some JSON (key = x, objects):
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x (turn JSON into PYTHON):
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

| JSON          | Python |
| :------------:|:------:|
| object        | dict   |
| array         | list   |
| string        | str    |
| number (int)  | int    |
| number (real) | float  |
| true          | True   |
| false         | False  |
| null          | None   |

Convert PYTHON into JSON:  
json.loads()    
```python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

extras:
```python
new_string = json.dumps(data)
# this just creates the JSON string
new_string = json.dumps(data, indent = 2)
# indent states the number of indentations per item in the string
new_string = json.dumps(data, indent = 2, sort_keys = True)
# sorts the keys alphabetically
```
| JSON.name                      | action                                      |
| :-----------------------------:|:-------------------------------------------:|
| json.dump(dict, file_pointer)  | writes to JSON file                         |
| json.dumps(python object)      | converts a python object into a JSON string |
| json.load(alias)               | loads a file into a python object           |
| json.loads(JSON string)        | loads a string into a python object         |
| with open(filename) as alias:  | opens a JSON file                            |
| with open(filename)            | opens a JSON file                           |  

NOTE: if the file is not in the same directory then the full path will be needed  
When opening files you can specify what you are wanting to do with them:  
r = read  
w = write  
a = append  
r+ = read and write  
rb = read binary mode  
wb = write binary mode  

READING:
```python
with open("filename.ext", "r") as alias:
    a = alias.read()  # reads the whole file
    b = alias.readlines()  # produces a list of all the lines
    c = alias.readline()  # grabs the first entry from a list of all the lines
    c = alias.readline()  # grabs the second entry from a list of all the lines
    print(c, end = "")  # end = "" prevents a new line being added after each statement
    d = alias.read(100)  # first 100 characters of file
    print(alias.tell())  # what position we are at in the file
    alias.seek(position)  # sets a position in the file

    
    for line in f:
        print(line, end = "")  # memory efficient because it doesn't read the whole file at once
```
WRITING:
```python
with open("filename.ext", "w") as alias:  # if the filename exist it will overwrite it and if it doesn't it will create it
   alias.write("blah")
# you can you "a" to append instead of overwrite as well.

with open("filename.ext", "r") as rf:  # we have opened file for reading
    with open("filename_copy.txt", "w") as wf:  # we have created a file for writing
        for line in rf:
            wf.write(line)  # iterate through and write each line to the new file

```
