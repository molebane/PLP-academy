import os

def create_and_write_file():
    try:
        # Specify a directory with write access
        file_path = os.path.join(os.path.expanduser('~'), 'my_file.txt')
        
        # Create a new text file and write initial content
        with open(file_path, 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("Here is the second line with a number: 12345\n")
            file.write("And the third line with some text.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating or writing to the file: {e}")
    finally:
        print("File creation and writing complete.")

def read_and_display_file():
    try:
        file_path = os.path.join(os.path.expanduser('~'), 'my_file.txt')
        
        # Read and display the contents of the file
        with open(file_path, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("File reading complete.")

def append_to_file():
    try:
        file_path = os.path.join(os.path.expanduser('~'), 'my_file.txt')
        
        # Append additional lines to the file
        with open(file_path, 'a') as file:
            file.write("Appending a new line.\n")
            file.write("Another new line added.\n")
            file.write("And one more line for good measure.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("File appending complete.")

# Execute the functions
create_and_write_file()
read_and_display_file()
append_to_file()
read_and_display_file()  # To display the file contents after appending
