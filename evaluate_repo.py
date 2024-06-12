import os

def list_all_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def create_blank_file_if_not_exists(filepath):
    if not os.path.exists(filepath):
        open(filepath, 'a').close()
        print(f'Created blank file: {filepath}')
    else:
        print(f'File already exists: {filepath}')

def evaluate_file(filepath):
    size = os.path.getsize(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
        if content.strip() == "":
            status = "Empty"
        else:
            status = "Contains content"
    return size, status

def main():
    # List of directories and files to check
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
    
    frontend_dir = "frontend/src"

    # Ensure necessary files exist
    for file in backend_files:
        create_blank_file_if_not_exists(file)
    
    # List all files in the repository
    all_files = list_all_files(".")

    # Generate the progress report
    with open("progress_report.md", "w") as report:
        report.write("# Progress Report\n\n")
        
        report.write("## List of all files in the repository\n")
        for file in all_files:
            report.write(f"- {file}\n")
        
        report.write("\n## Server Connection.Py\n")
        size, status = evaluate_file("backend/server_connection.py")
        report.write(f"- backend/server_connection.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Site Scraper.Py\n")
        size, status = evaluate_file("backend/site_scraper.py")
        report.write(f"- backend/site_scraper.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Single Family Evaluation.Py\n")
        size, status = evaluate_file("backend/single_family_evaluation.py")
        report.write(f"- backend/single_family_evaluation.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Multi Family Evaluation.Py\n")
        size, status = evaluate_file("backend/multi_family_evaluation.py")
        report.write(f"- backend/multi_family_evaluation.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Email Contact.Py\n")
        size, status = evaluate_file("backend/email_contact.py")
        report.write(f"- backend/email_contact.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Property Management.Py\n")
        size, status = evaluate_file("backend/property_management.py")
        report.write(f"- backend/property_management.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Log Section.Py\n")
        size, status = evaluate_file("backend/log_section.py")
        report.write(f"- backend/log_section.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Offer Generator.Py\n")
        size, status = evaluate_file("backend/offer_generator.py")
        report.write(f"- backend/offer_generator.py exists.\n- Size: {size} bytes\n- Status: {status}\n\n")

        report.write("## Frontend\n")
        size = sum(os.path.getsize(f) for f in list_all_files(frontend_dir))
        report.write(f"- {frontend_dir} exists.\n- Size: {size} bytes\n")

if __name__ == "__main__":
    main()