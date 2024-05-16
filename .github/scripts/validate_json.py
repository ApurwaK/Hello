import json
import os

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            print(f"{file_path}: Valid JSON format")
            return True
    except Exception as e:
        print(f"{file_path}: Invalid JSON format - {str(e)}")
        return False

def main():
    # Determine the directory path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the json files directory relative to the script's location
    json_dir = os.path.join(script_dir, '..', 'workflows')

    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir, filename)
            validate_json(file_path)

if __name__ == "__main__":
    main()

