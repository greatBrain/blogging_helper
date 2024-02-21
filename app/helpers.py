#Helper functions that may be used in any part of the code.
import os



def check_dir_exists(dir_name) -> bool:

    global directory    
    directory = dir_name

    if not os.path.exists(dir_name):
       os.mkdir(dir_name)       
    return True


def delete_files() -> bool:    
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)
        os.remove(file_path)
    return True