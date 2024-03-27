# Remitly-Internship-2024
> Repository with programming task for 2024 summer intern at Remitly.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)


## General Information
- Parser developed for checking `["Resource"]` field in AWS::IAM::Role Policy JSON file.
- Due to variations in the policy file structure (sometimes policy may contain multiple statements, each with its own resource), I allowed myself to change the return value. Instead of a single boolean, the function now returns a list of booleans to cover edge cases.
- Unit tests are also provided.


## Technologies Used
- Python 3.12


## Setup
Python 3.12 interpreter is the only condition needed to run the script. All libraries used in script, are standard python libraries, therefore it is unnecessary to install any requirements.

## Usage
- User has at his disposal directory with sample JSON files to check how the script works.
- Only place in code, that requires changes is `file_path` variable in **main.py** file . User needs to enter correct file path to check other samples or own JSON files.
- To execute the script go into **root** directory and type in terminal `python3 main.py`.
  ### Tests
- When someone wishes to make changes in code, it is recommended to run prepared unit tests, to inspect if adjustments did not affect the script functionality correctness.
- To run tests go into **tests** directory and type in terminal `python3 test_json_parser.py`.



