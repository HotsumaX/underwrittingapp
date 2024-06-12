import os

def create_blank_file_if_not_exists(path):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write("")
        print(f"Created blank file: {path}")
    else:
        print(f"File already exists: {path}")

def list_directory_contents(directory):
    try:
        files = os.listdir(directory)
        print(f"Contents of {directory}:")
        for file in files:
            print(f" - {file}")
    except FileNotFoundError:
        print(f"Directory {directory} does not exist.")

def generate_progress_report():
    # Paths to relevant directories and files
    paths = {
        'server_connection': 'backend/server_connection.py',
        'site_scraper': 'backend/site_scraper.py',
        'single_family_evaluation': 'backend/single_family_evaluation.py',
        'multi_family_evaluation': 'backend/multi_family_evaluation.py',
        'email_contact': 'backend/email_contact.py',
        'property_management': 'backend/property_management.py',
        'log_section': 'backend/log_section.py',
        'offer_generator': 'backend/offer_generator.py',
        'frontend': 'frontend/src'
    }

    report = []
    report.append("# Progress Report\n")

    # List contents of the backend directory
    list_directory_contents('backend')
    list_directory_contents('frontend/src')

    for feature, path in paths.items():
        print(f"Checking {path}...")  # Debugging: Print path being checked
        report.append(f"## {feature.replace('_', ' ').title()}\n")
        create_blank_file_if_not_exists(path)  # Create blank file if not exists
        if os.path.exists(path):
            report.append(f"- {path} exists.\n")
            report.append(f"- Size: {os.path.getsize(path)} bytes\n")
            print(f" - {path} exists.")  # Debugging: Confirm existence
        else:
            report.append(f"- {path} does not exist.\n")
            print(f" - {path} does not exist.")  # Debugging: Confirm non-existence
        report.append("\n")

    with open("progress_report.md", "w") as report_file:
        report_file.write("\n".join(report))

    # Append the report to README.md
    with open("README.md", "a") as readme_file:
        readme_file.write("\n".join(report))

    # Debugging: Print the generated report to the console
    print("\n".join(report))

if __name__ == "__main__":
    generate_progress_report()