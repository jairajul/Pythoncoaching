#Task 1: Read a File and Handle Errors
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                print(f"Line {idx}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The File '{filename}' was not found.")

read_file("sample.txt")


#Task 2: Write and Append Data to a File
def write_to_file(filename):
    user_input = input("Hello, Python! ")
    with open(filename, "w") as file:
        file.write(user_input + "\n")

def append_to_file(filename):
    additional_input = input("Learning file handling in Python.")
    with open(filename, "a") as file:
        file.write(additional_input + "\n")

def read_file(filename):
    print("Hello, Python! \n Learning file handling in Python.")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

filename = 'output.txt'
write_to_file(filename)
append_to_file(filename)
read_file(filename)




