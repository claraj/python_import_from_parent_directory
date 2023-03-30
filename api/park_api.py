# This file is intended to be imported and used by the main module, 
# and then the imports are assumed to be relative to the location of the main.py
# file. So, when this file is imported by main, then all the imports listed should 
# be relative to where main is, so this works,
# from model.park import Park 

# But, if we want to run this file by itself, for testing it at the commanf prompt, 
# the import won't work, since 
# the imports are relative to the location of this file, and 
# from model.park import Park 
# looks for a subdirectory called model in the api directory, where this file is, that doesn't exist.

# So, we need to add the parent directory to the Python Path, the list of directories 
# that Python looks in when it imports other modules. 

from pathlib import Path
import sys
 
# __file__ is a special string variable storing the location of this file on the computer that is running this program 
path_to_this_code_file = Path(__file__)  # Create a Path object 
# Need a reference the base directory of this project, relative to this file
# Here, the parent of this file is the model directory, the parent of the model directory is the project base ent 
project_base_directory = path_to_this_code_file.parent.parent  # creates a Path object representing the location of the project base directory 

# sys.path is a list of locations that the python import system checks for modules and files 
# If a module or package exists in one of these locations, it can be imported 
# The path should be a list of strings, so convert the Path to a string,
sys.path.append(str(project_base_directory))

# Now this import works when this code is imported from main.py and when this file is run by itself 
from model.park import Park 

def get_park():
    return Park('Grand Canyon')


# To run this file by itself for testing, using the default Python path, the import statement 
# from model.park import Park 
# would fail, since the model directory is above this one. 
# Unless we modify the path - a list of locations that Python checks for files to import 

if __name__ == '__main__':
    park = get_park()
    print(park.name)