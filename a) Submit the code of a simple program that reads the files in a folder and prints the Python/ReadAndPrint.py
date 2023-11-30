import os

def print_and_comment_python_files(folder_path):
    # Iterate through each file in the specified folder path
    for filename in os.listdir(folder_path):
        # Check if the file has a ".py" extension
        if filename.endswith(".py"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Print the file path to the console
            print(file_path)

            # Open the file in append mode
            with open(file_path, "a") as target:
                # Add comments at the end of the file
                target.write("\n\n# Hey, This is a python file\n")

if __name__ == "__main__":
    # Prompt the user to enter the folder path
    folder_path = input("Enter the folder path: ")
    
    # Print a message indicating the operation
    print("Python source files in the folder:")
    
    # Call the function to print file paths and add comments
    print_and_comment_python_files(folder_path)
