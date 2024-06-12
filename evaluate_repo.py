import os

def evaluate_repo():
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

    frontend_path = "frontend/src"

    progress_report = "# Progress Report\n\n"

    for file in backend_files:
        file_path = os.path.join("backend", file)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            progress_report += f"## {file.replace('_', ' ').title()}\n\n"
            progress_report += f"- backend/{file} exists.\n\n"
            progress_report += f"- Size: {size} bytes\n\n"
        else:
            with open(file_path, 'w') as f:
                pass
            progress_report += f"## {file.replace('_', ' ').title()}\n\n"
            progress_report += f"- backend/{file} created.\n\n"
            progress_report += f"- Size: 0 bytes\n\n"

    if os.path.exists(frontend_path):
        size = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, filenames in os.walk(frontend_path) for f in filenames)
        progress_report += "## Frontend\n\n"
        progress_report += f"- frontend/src exists.\n\n"
        progress_report += f"- Size: {size} bytes\n\n"
    else:
        progress_report += "## Frontend\n\n"
        progress_report += "- frontend/src does not exist.\n\n"

    # Write the progress report to progress_report.md
    with open("progress_report.md", "w") as f:
        f.write(progress_report)

    # Update the README.md file
    readme_content = ""
    with open("README.md", "r") as f:
        readme_content = f.read()

    if "# Progress Report" in readme_content:
        readme_content = readme_content.split("# Progress Report")[0]

    readme_content += progress_report

    with open("README.md", "w") as f:
        f.write(readme_content)

if __name__ == "__main__":
    evaluate_repo()