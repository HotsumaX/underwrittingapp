import os

def check_and_create_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            pass
        print(f"Created blank file: {filepath}")
    else:
        print(f"File already exists: {filepath}")

def get_file_status(filepath):
    if os.path.getsize(filepath) == 0:
        return "Empty"
    else:
        with open(filepath, 'r') as file:
            content = file.read().strip()
        if not content:
            return "Empty"
        else:
            return "Has content"

def generate_file_list(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_list.append(filepath)
    return file_list

def evaluate_files(filepaths):
    evaluation = ""
    for filepath in filepaths:
        status = get_file_status(filepath)
        evaluation += f"- {filepath} exists.\n- Size: {os.path.getsize(filepath)} bytes\n- Status: {status}\n\n"
    return evaluation

def main():
    backend_files = [
        'backend/server_connection.py',
        'backend/site_scraper.py',
        'backend/single_family_evaluation.py',
        'backend/multi_family_evaluation.py',
        'backend/email_contact.py',
        'backend/property_management.py',
        'backend/log_section.py',
        'backend/offer_generator.py'
    ]

    for file in backend_files:
        check_and_create_file(file)

    file_list = generate_file_list(".")
    file_list_str = "\n".join([f"- {file}" for file in file_list])

    backend_evaluation = evaluate_files(backend_files)
    frontend_evaluation = evaluate_files(['frontend/src'])

    progress_report = f"# Progress Report\n\n## List of all files in the repository\n{file_list_str}\n\n"
    progress_report += "## Server Connection\n" + backend_evaluation + "\n"
    progress_report += "## Frontend\n" + frontend_evaluation + "\n"

    with open('progress_report.md', 'w') as file:
        file.write(progress_report)

    with open('README.md', 'w') as file:
        file.write(progress_report)

if __name__ == "__main__":
    main()