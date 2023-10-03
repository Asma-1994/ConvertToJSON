import csv
import json
from jinja2 import Template
import os
import glob
# Define the CSV input file and JSON output file
csv_file = 'sample.csv'
json_file = 'output.json'
template_file = 'template.json.j2'
json_dummy ='json.json'

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

def list_files_recursively(folder_path):
    file_names = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_names.append(file_name)
    return file_names


# File split logic 
answer = input("Do you want to split file in brunt repository, Say yes or no ")
if(answer == 'yes' or answer == 'YES' or answer == 'Yes') : 
    folder_path = input("Enter the brunt repository test suite path here : ")  # Replace with the path to the folder you want to list files from

    # List all files in the specified folder
    file_names = list_files_recursively(folder_path)
    # for file_name in file_names:
    #     print(file_name)
create_folder = input("Do you wish to create folder - yes or no")


for item in data:
    module_name = item["name"]
    module_name = module_name.replace(" ", "-").replace(",", "-").lower()  # Replace spaces with underscores
    new_filename = f"{module_name}.json"
    file_path = os.path.join(folder_path, new_filename)

    # Check if the file already exists
    if os.path.isfile(file_path):
        print(f'File with JSON file name "{new_filename}" already exists. Skipping...')
    else:
        with open(file_path, "w") as outfile:
            json.dump(item, outfile, indent=4)
        print(f'JSON data has been written to "{file_path}"')




for item in data:
    module_name = item["name"]
    module_name = module_name.replace(" ", "-").replace(",", "-").lower()  # Replace spaces with underscores
    new_filename = f"{module_name}.json"
    for if_file_exist in file_names:
        if(if_file_exist == new_filename):
            print(f'File with json file name {if_file_exist} ' + " already exist ")
        else:
            with open(new_filename, "w") as outfile:
                json.dump(item, outfile, indent=4)
    break



# /Users/asmakhan/Desktop/brunt/todo-cases/future-case


        #    if (create_folder == 'no' or create_folder == 'NO' or create_folder == 'No' ):
        #         push_json_directory_path = os.path.join(folder_path, new_folder_name)
        #         push_json_file_path = os.path.join(push_json_directory_path,new_filename)
        #         with open(push_json_file_path, "w") as outfile:
        #             json.dump(item, outfile, indent=4) 
        #             print(f'JSON test suite for scenario {new_filename} created') 
        #     elif (create_folder == 'Yes' or create_folder == 'YES' or create_folder == 'yes' ):
        #         new_folder_name = input("Write name of folder to be created").replace(" ", "-").lower()
        #         path = os.path.join(folder_path, new_folder_name)
        #         if not os.path.exists(path):
        #             os.mkdir(path)
        #             os.chdir(path)
        #             with open(file_name, "w") as outfile:
        #                 json.dump(item, outfile, indent=4)
