import os

# Define the directory and file list
repo_dir = os.getcwd()
file_list = []

for root, dirs, files in os.walk(repo_dir):
    for file in files:
        file_list.append(os.path.relpath(os.path.join(root, file), repo_dir))

# Generate progress report content
progress_report_content = "# Progress Report\n\n## List of all files in the repository\n"
for file in file_list:
    progress_report_content += f"- {file}\n"

# List of backend files to check
backend_files = [
    "backend/server_connection.py",
    "backend/site_scraper.py",
    "backend/single_family_evaluation.py",
    "backend/multi_family_evaluation.py",
    "backend/email_contact.py",
    "backend/property_management.py",
    "backend/log_section.py",
    "backend/offer_generator.py"
]

# Add backend file checks to the report
for backend_file in backend_files:
    if os.path.exists(backend_file):
        size = os.path.getsize(backend_file)
        progress_report_content += f"\n## {os.path.basename(backend_file).replace('_', ' ').title()}\n\n- {backend_file} exists.\n\n- Size: {size} bytes\n"
    else:
        with open(backend_file, 'w') as f:
            pass
        progress_report_content += f"\n## {os.path.basename(backend_file).replace('_', ' ').title()}\n\n- Created blank file: {backend_file}\n\n- Size: 0 bytes\n"

# Check frontend directory
frontend_dir = "frontend/src"
if os.path.exists(frontend_dir):
    size = sum(os.path.getsize(os.path.join(root, file)) for root, _, files in os.walk(frontend_dir) for file in files)
    progress_report_content += f"\n## Frontend\n\n- {frontend_dir} exists.\n\n- Size: {size} bytes\n"

# Write the progress report to progress_report.md
with open("progress_report.md", "w") as f:
    f.write(progress_report_content)

# Replace the content of README.md with the progress report
with open("README.md", "w") as f:
    f.write(progress_report_content)