import os

def list_files_in_repo(root_dir='.'):
    file_list = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if '.git' not in root:
                file_list.append(os.path.relpath(os.path.join(root, file), root_dir))
    return file_list

def evaluate_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        return f"- {file_path} does not exist. Created blank file: {file_path}.\n"
    else:
        size = os.path.getsize(file_path)
        return f"- {file_path} exists.\n- Size: {size} bytes\n"

def evaluate_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return f"- {directory_path} does not exist. Created directory: {directory_path}.\n"
    else:
        size = sum(os.path.getsize(os.path.join(directory_path, f)) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f)))
        return f"- {directory_path} exists.\n- Size: {size} bytes\n"

def generate_report():
    report = "# Progress Report\n\n"

    # List all files in the repo
    report += "## List of all files in the repository\n\n"
    file_list = list_files_in_repo()
    for file in file_list:
        report += f"- {file}\n"
    report += "\n"

    sections = {
        "Server Connection": ["backend/server_connection.py"],
        "Site Scraper": ["backend/site_scraper.py"],
        "Single Family Evaluation": ["backend/single_family_evaluation.py"],
        "Multi Family Evaluation": ["backend/multi_family_evaluation.py"],
        "Email Contact": ["backend/email_contact.py"],
        "Property Management": ["backend/property_management.py"],
        "Log Section": ["backend/log_section.py"],
        "Offer Generator": ["backend/offer_generator.py"],
        "Frontend": ["frontend/src"]
    }

    for section, paths in sections.items():
        report += f"## {section}\n\n"
        for path in paths:
            if path.endswith('/'):
                report += evaluate_directory(path)
            else:
                report += evaluate_file(path)
        report += "\n"

    with open("progress_report.md", "w") as f:
        f.write(report)

    with open("README.md", "w") as f:
        f.write(report)

if __name__ == "__main__":
    generate_report()