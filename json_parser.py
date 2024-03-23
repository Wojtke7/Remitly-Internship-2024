import json


def json_parser(file_path: str):
        
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

    # Try block to check if the file structure is valid AWS Policy JSON 
    try:
        policy_body = data["PolicyDocument"]
        # Check if key is present
        policy_body["Version"]
        # It is possible that policy file contains multiple statements
        statements = policy_body["Statement"]
        # Because of multiple resources (one per statement), we provide a list to store multiple logical values
        bool_list = []
        for statement in statements:
            # Check if keys are present
            statement["Effect"]
            statement["Action"]

            if statement["Resource"] != "*":
                bool_list.append(True)
            else:
                bool_list.append(False)

    except KeyError:
        raise KeyError("File has invalid AWS Policy document structure.")

    return bool_list
