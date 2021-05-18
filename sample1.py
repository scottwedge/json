#!/usr/bin/env python3

# Fooling around with JSON data formats

# after 'import json', use json.dumps() to print formatted output
# and json.loads() to read formatted input

# Great documentation in help(json.dumps) and help(json.loads)

# Imports
import json
import time


# Define variables
file = "/tmp/t"
d1 = {"oldest":"Scott", "youngest":"Allan"}
l1 = [1, 2, 3, 4]
s = "long_string"


# Convert to JSON format
j = json.dumps(d1, indent = 4)
print(j)

f = open(file, "w")
f.write(j + "\n")
f.write(s + "\n")
f.close()



