import os
import subprocess

files = [
    "backend/server_connection.py",
    "backend/site_scraper.py",
    "backend/scrape_zillow_with_selenium.py",
    "backend/single_family_evaluation.py",
    "backend/multi_family_evaluation.py",
    "backend/offer_generator.py"
]

docstrings = {
    "backend/server_connection.py": "\"\"\"Module to handle server connections.\"\"\"",
    "backend/site_scraper.py": "\"\"\"Module to scrape websites.\"\"\"",
    "backend/scrape_zillow_with_selenium.py": "\"\"\"Module to scrape Zillow using Selenium.\"\"\"",
    "backend/single_family_evaluation.py": "\"\"\"Module for single-family property evaluation.\"\"\"",
    "backend/multi_family_evaluation.py": "\"\"\"Module for multi-family property evaluation.\"\"\"",
    "backend/offer_generator.py": "\"\"\"Module to generate property offers.\"\"\"",
}

# Step 1: Ensure requests and selenium are installed
def install_packages():
    subprocess.run(["pip", "install", "requests", "selenium"])

# Step 2: Add missing module docstrings, newlines, and ensure correct number of blank lines before functions/classes
def add_docstrings_and_newlines():
    for file in files:
        with open(file, 'r') as f:
            content = f.readlines()

        if not content[0].startswith("\"\"\""):
            content.insert(0, docstrings[file] + "\n\n")

        # Ensure two blank lines before function and class definitions, but not more
        new_content = []
        for line in content:
            if line.startswith("def ") or line.startswith("class "):
                if len(new_content) > 1 and new_content[-1].strip() == "" and new_content[-2].strip() == "":
                    # Already has two blank lines, so add the line as it is
                    new_content.append(line)
                else:
                    # Add two blank lines before the function/class definition
                    new_content.append("\n\n" + line)
            else:
                # Remove excess blank lines
                if line.strip() == "" and (len(new_content) > 0 and new_content[-1].strip() == ""):
                    continue
                new_content.append(line)

        # Ensure the file ends with exactly one newline
        if not new_content[-1].endswith('\n'):
            new_content.append('\n')
        elif new_content[-1] == '\n' and new_content[-2] == '\n':
            new_content = new_content[:-1]

        with open(file, 'w') as f:
            f.writelines(new_content)
        print(f"Updated {file}")

# Step 3: Verify changes
def verify_changes():
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        if not content.startswith(docstrings[file]):
            print(f"{file} docstring is incorrect")
        if not content.endswith('\n'):
            print(f"{file} does not end with a newline")
        if "def " in content or "class " in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith("def ") or line.startswith("class "):
                    if i > 1 and (lines[i-1].strip() or lines[i-2].strip()):
                        print(f"{file} does not have two blank lines before {line}")
        else:
            print(f"{file} content is correct")

# Step 4: Run improve_project.py
def run_improve_project():
    subprocess.run(["python3", "improve_project.py"])

if __name__ == "__main__":
    install_packages()
    add_docstrings_and_newlines()
    verify_changes()
    run_improve_project()