def read_and_modify_file():
    
    input_file = input("Enter the name of the file to read: ")

    try:
        
        with open(input_file, 'r') as file:
            content = file.read()

        
        modified_content = content.upper()

        
        output_file = "modified_" + input_file

        
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()
