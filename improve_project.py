"""
Module docstring
"""

import subprocess
import glob

def run_command(command):
    """Function docstring"""
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout if result.stdout else result.stderr

def get_all_python_files():
    """Get a list of all Python files in the repository"""
    return glob.glob('**/*.py', recursive=True)

def main():
    python_files = get_all_python_files()
    
    for file_path in python_files:
        print(f"Running checks on: {file_path}")
        print(run_command(['flake8', file_path]))
        print(run_command(['pylint', file_path]))
        print(run_command(['bandit', file_path]))

    # Clean up and optimize codebase
    print(run_command(['python3', 'cleanup_script.py']))

if __name__ == "__main__":
    main()