import os

# Paths to files and directories
app_outline_path = 'appoutline.txt'
progress_report_path = 'progress_report.md'
readme_path = 'README.md'
backend_dir = 'backend'
frontend_dir = 'frontend/src'

# Files to check in backend
backend_files = [
    'server_connection.py',
    'site_scraper.py',
    'single_family_evaluation.py',
    'multi_family_evaluation.py',
    'email_contact.py',
    'property_management.py',
    'log_section.py',
    'offer_generator.py'
]

# Function to check file existence and create if not present
def check_and_create_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        print(f'Created blank file: {filepath}')
    else:
        print(f'File already exists: {filepath}')
    return os.path.exists(filepath)

# Function to generate progress report
def generate_progress_report():
    progress_report = "# Progress Report\n\n"

    # Check backend files
    for file in backend_files:
        file_path = os.path.join(backend_dir, file)
        exists = check_and_create_file(file_path)
        file_size = os.path.getsize(file_path) if exists else 0
        progress_report += f"## {file.replace('_', ' ').title()}\n\n"
        progress_report += f"- {file_path} {'exists' if exists else 'does not exist'}.\n\n"
        progress_report += f"- Size: {file_size} bytes\n\n"

    # Check frontend directory
    exists = os.path.exists(frontend_dir)
    dir_size = sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(frontend_dir) for file in files) if exists else 0
    progress_report += "## Frontend\n\n"
    progress_report += f"- {frontend_dir} {'exists' if exists else 'does not exist'}.\n\n"
    progress_report += f"- Size: {dir_size} bytes\n\n"

    return progress_report

# Write progress report to file
progress_report = generate_progress_report()
with open(progress_report_path, 'w') as f:
    f.write(progress_report)
print(f"Progress report generated in {progress_report_path}")

# Update README.md
if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        readme_content = f.read()

    # Remove old progress report
    if "## Progress Report" in readme_content:
        readme_content = readme_content.split("## Progress Report")[0].strip()

    with open(readme_path, 'w') as f:
        f.write(readme_content + '\n\n' + progress_report)
    print(f"README.md updated with new progress report")

# Update app outline
if os.path.exists(app_outline_path):
    with open(app_outline_path, 'a') as f:
        f.write(progress_report)
    print(f"App outline updated with new progress report")