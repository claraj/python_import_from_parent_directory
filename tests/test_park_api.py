
# Add base directory of the project to the path.

# Allows this file to be run by itself from the terminal in the tests directory, 
# python park_api_test

# Or, it can be run from the base directory of this project
# python -m unittest tests.park_api_test
# Or, all test files here
# python -m unittest discover tests

from pathlib import Path
import sys
 
path_to_this_code_file = Path(__file__)  # A Path object representing this file's location
project_base_directory = path_to_this_code_file.parent.parent  # A Path object representing the base directory of the project
sys.path.append(str(project_base_directory))  # Add the string version of the project_base_directory to the python path 

# Imports are relative to base directory of project 

from model.park import Park 
import unittest 
from unittest import TestCase 


class TestPark(TestCase):

    def test_park_name(self):
        p = Park('Yosemite')
        self.assertEqual('Yosemite', p.name)



if __name__ == '__main__':
    # Without mod
    unittest.main()