import sys
import os

# Add the path to the parent directory to sys.path
modules_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modules_dir_path)

# Import packages from parent directory:
import mod_a as ModA 
import mod_b as ModB


