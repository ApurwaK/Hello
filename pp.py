import json

with open("student.json", "r") as read_file:
    print("Read JSON file")
    student = json.load(read_file)

    print("Before Pretty Printing JSON Data")
    print(student)

    print("\n")

    PrettyJson = json.dumps(student, indent=4, separators=(',', ': '), sort_keys=True)
    print("Displaying Pretty Printed JSON Data")
    print(PrettyJson)
