"""
Name: Jakob West 
Class: DASE 1011-001 
Due: Friday, October 6th, 2023 @ 11:59 PM 
Assignment: Lab 2 
Description: This Python code creates a general JSON Schema,
processes each row in the auto-mpg.data-original.csv file,
collects JSON objects in an array, and generates the JSON results
in order to help us gain a solid understanding of devloping JSON
schemas and the application of these schemas inside of Python. I chose
to do entire Python program to strengthen my understanding. 
"""


import csv
import json


'''
Part #1: Create the JSON Schema
'''

json_schema = {

    "type": "object",
    "properties": {
        
        "ID": {"type": "integer"},
        "mpg": {"type": "number"},
        "cylinders": {"type": "integer"},
        "displacement": {"type": "number"},
        "horsepower": {"type": "number"},
        "weight": {"type": "number"},
        "acceleration": {"type": "number"},
        "model year": {"type": "integer"},
        "origin": {"type": "integer"},
        "car name": {"type": "string"},

    }, # end properties

    "required": ["ID", "mpg", "cylinders", "displacement",
                 "horsepower", "weight", "acceleration",
                 "model year", "origin", "car name"]

} # end json_schema



'''
Part #2: Process the CSV file and generate JSON result
'''

json_results = []


with open('auto-mpg.data-original.csv', mode='r') as json_csv:

    csv_reader = csv.DictReader(json_csv)

    for row in csv_reader:

        json_results.append(row)



'''
Part #3: Output the entire JSON result (Answer for Part 1A)
'''

with open ('output.json', mode='w') as json_file:

    json.dump(json_results, json_file)
