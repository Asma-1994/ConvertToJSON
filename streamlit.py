import csv
import json
from jinja2 import Template
import os
import sys
# Define the CSV input file and JSON output file
csv_file = input("Enter Sample CSV file name ")+'.csv'
json_file = 'output.json'
template_file = 'template.json.j2'

# Initialize an empty list to store the data
data = []

import re

def remove_ascii_and_escape(input_str):
    # Use regex to remove non-ASCII characters
    ascii_removed = re.sub(r'[^\x00-\x7F]+', '', input_str)
    
    # Use Python's built-in escape sequences to remove escape characters
    escaped_removed = ascii_removed.encode('utf-8').decode('unicode_escape')
    
    return escaped_removed
# Read data from the CSV file and append it to the list
with open(csv_file, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Read the Jinja2 template
with open(template_file, 'r') as template_file:
    template_content = template_file.read()

# Create a Jinja2 template
template = Template(template_content)
# Render the template with the CSV data
json_data = template.render(tasks=data)

#print(json_data)

json_object = json.loads(json_data)

# Write the data as JSON to the output file
with open(json_file, 'w') as json_file:
    json.dump(json_object, json_file, indent=4)

# Read JSON data from a file
with open('output.json', 'r') as input_file:
    data = json.load(input_file)

print("JSON file is created, please validated...!!!")

# function to regressively check for file in brunt repository
def list_files_recursively(folder_path,suite_name):
    file_names = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name == suite_name:
                print(f'File with JSON file name "{suite_name}" already exists. Skipping...')
                return False
    return True


# File split logic 
repo_path = input("Enter the brunt repository test suite path here : ")  # Replace with the path to the folder you want to list files from
module_folder = input("Enter module name of folder where you want to add JSON Test Suites ")
folder_path = os.path.join(repo_path,'todo-cases/future-case')
module_folder_path = os.path.join(folder_path, module_folder)

# Check if Module folder exist in brunt project 

if(os.path.exists(module_folder_path)):
    print(f'Found Module Folder named {module_folder}')
else :
    print("Seems like Module folder does not exist ....!!!")
    should_create_new_folder = input("Do you want to Create Module Folder, Say yes or no ? ")

    # create folder if user add yes in prompt 
    if(should_create_new_folder == 'yes' or should_create_new_folder == 'YES' or should_create_new_folder == 'Yes'):
        module_folder_name = input("Enter the name of the module Folder to be created ").lower()
        path = os.path.join(folder_path, module_folder_name)
        os.mkdir(path)
    else :
        # if user does not want to create module folder exit program
        print("Exiting the program.")
        sys.exit()

for item in data:
    module_name = item["name"]
    module_name = module_name.replace(" ", "-").replace(",", "-").lower()  # Replace spaces with underscores
    new_filename = f"{module_name}.json"
    is_file_exist = list_files_recursively(repo_path,new_filename)
    if(is_file_exist):
        file_path = os.path.join(folder_path, module_folder, new_filename)
        with open(file_path, "w") as outfile:
            json.dump(item, outfile, indent=4)
            print(f'JSON data has been written to "{new_filename}" ')






# /Users/asmakhan/Desktop/brunt/todo-cases/future-case

