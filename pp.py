
import json

def validate_json_file(Menu.json):
    try:
        with open(file_path, 'r') as file:
            json_data = file.read()
            parsed_data = json.loads(json_data)
        print("The JSON file is valid.")
        return True, parsed_data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
        return False, None
    except FileNotFoundError:
        print("The specified file was not found.")
        return False, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return False, None

# Example usage:
file_path = 'Menu.json'
is_valid, data = validate_json_file(file_path)

