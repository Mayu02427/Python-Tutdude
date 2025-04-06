def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:")
            for line in file:
                print(line.strip())  # Remove extra newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Calling the function with the filename
read_file('sample.txt')