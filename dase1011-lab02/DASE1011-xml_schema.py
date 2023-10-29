"""
Name: Jakob West 
Class: DASE 1011-001 
Due: Friday, October 6th, 2023 @ 11:59 PM 
Assignment: Lab 2 
(Part 1B - XML)
Description: This Python code builds the XML Schema inside the code
following XML general practices and outputs results to a file
in order to help us gain a solid understanding of devloping XML
schemas and the application of these schemas inside of Python. I chose
to do entire Python program to strengthen my understanding. 
"""


import csv


'''
Part #1: Read in the CSV file and generate XML schema using double for loops
'''

# define root element (xml version and encoding)
xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n<vehicles>\n'


with open('auto-mpg.data-original.csv', mode='r') as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        
        xml_string += '  <vehicle>\n'
        
        for key, value in row.items():
            
            xml_string += f'    <{key}>{value}</{key}>\n'

        xml_string += '  </vehicle>\n'

# Close the root element
xml_string += '</vehicles>'



'''
Part #2: Save the results to a new XML file
'''

with open('output.xml', mode='w') as xml_file:
    xml_file.write(xml_string)
