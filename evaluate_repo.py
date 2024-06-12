import os

def check_and_create(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(f"# {os.path.basename(file_path)}\n")
        print(f"Created blank file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

def main():
    backend_files = [
        "server_connection.py",
        "site_scraper.py",
        "single_family_evaluation.py",
        "multi_family_evaluation.py",
        "email_contact.py",
        "property_management.py",
        "log_section.py",
        "offer_generator.py"
    ]

    report = "# Progress Report\n\n"

    for file in backend_files:
        file_path = os.path.join("backend", file)
        check_and_create(file_path)
        report += f"## {file.replace('_', ' ').title()}\n\n"
        report += f"- {file_path} exists.\n\n"
        report += f"- Size: {os.path.getsize(file_path)} bytes\n\n"

    frontend_path = "frontend/src"
    if os.path.exists(frontend_path):
        report += "## Frontend\n\n"
        report += f"- {frontend_path} exists.\n\n"
        report += f"- Size: {sum(os.path.getsize(os.path.join(root, name)) for root, _, files in os.walk(frontend_path) for name in files)} bytes\n\n"

    # Write the report to progress_report.md
    with open("progress_report.md", "w") as report_file:
        report_file.write(report)
    
    # Update the README.md file
    readme_content = ""
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r") as readme_file:
            readme_content = readme_file.read()
    
    with open(readme_path, "w") as readme_file:
        readme_file.write(report + readme_content)

if __name__ == "__main__":
    main()