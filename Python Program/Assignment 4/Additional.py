def write_to_file(filename):
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data written to file.")

def append_to_file(filename):
    more_data = input("Ente"
                      "r additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(more_data + '\n')
    print("Additional data appended to file.")

def read_file(filename):
    print("\nFinal content of the file:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# File name
filename = 'output.txt'

# Function calls
write_to_file(filename)
append_to_file(filename)
read_file(filename)
