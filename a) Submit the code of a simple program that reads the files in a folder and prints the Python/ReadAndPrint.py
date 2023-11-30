import os

def print_and_comment_python_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            print(file_path)

            with open(file_path, "a") as target:
                target.write("\n\n# Hey, This is a python file\n")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    print("Python source files in the folder:")
    print_and_comment_python_files(folder_path)





