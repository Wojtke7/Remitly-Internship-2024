import json


def check_json_resource(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)

        # It is possible that JSON file contains multiple statements
        statements = len(data["PolicyDocument"]["Statement"])
        print(statements)

        # Because of multiple resources we need multiple logical statements stored in list
        bool_list = []

        for i in range(statements):
            if data["PolicyDocument"]["Statement"][i]["Resource"] != "*":
                print(data["PolicyDocument"]["Statement"][i]["Resource"])
                bool_list.append(True)
            else:
                print(data["PolicyDocument"]["Statement"][i]["Resource"])
                bool_list.append(False)

        return bool_list


print(check_json_resource("JSON files/test6.json"))
