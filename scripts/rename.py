import os


def replace_question_mark(str):
    try:
        return str[0:str.index("%3")]
    except:
        return str

def fix_file_name(filename):
    new_file_path = replace_question_mark(filename)
    if filename != new_file_path:
        print(filename)
        os.rename(filename, new_file_path)

def rewrite_files(folder = os.getcwd()):
    for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            filepath = subdir + os.sep + file
            fix_file_name(filepath)
            
def main():
    rewrite_files()
    
if __name__ == "__main__":
    main()