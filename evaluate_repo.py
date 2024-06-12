import os

def list_files(startpath):
    files_list = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def get_file_status(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines), "File read successfully."
    except Exception as e:
        return 0, f"Error reading file: {e}"

def evaluate_files(files):
    evaluations = []
    for filepath in files:
        lines, status = get_file_status(filepath)
        evaluation = {
            'path': filepath,
            'lines': lines,
            'status': status,
            'importance': 'TBD',  # Placeholder for importance rating
            'comments': 'TBD'  # Placeholder for comments
        }
        evaluations.append(evaluation)
    return evaluations

def categorize_files(files):
    categories = {
        'Server Connection': [],
        'Site Scraper': [],
        'Single Family Evaluation': [],
        'Multi Family Evaluation': [],
        'Email Contact': [],
        'Property Management': [],
        'Log Section': [],
        'Offer Generator': [],
        'Frontend': [],
        'Miscellaneous': [],
    }
    for file in files:
        if 'server_connection' in file['path']:
            categories['Server Connection'].append(file)
        elif 'scrape' in file['path']:
            categories['Site Scraper'].append(file)
        elif 'single_family' in file['path']:
            categories['Single Family Evaluation'].append(file)
        elif 'multi_family' in file['path']:
            categories['Multi Family Evaluation'].append(file)
        elif 'email_contact' in file['path']:
            categories['Email Contact'].append(file)
        elif 'property_management' in file['path']:
            categories['Property Management'].append(file)
        elif 'log' in file['path']:
            categories['Log Section'].append(file)
        elif 'offer_generator' in file['path']:
            categories['Offer Generator'].append(file)
        elif 'frontend' in file['path']:
            categories['Frontend'].append(file)
        else:
            categories['Miscellaneous'].append(file)
    return categories

def main():
    repo_path = '.'
    repo_files = list_files(repo_path)
    evaluations = evaluate_files(repo_files)
    categories = categorize_files(evaluations)

    with open('progress_report.md', 'w', encoding='utf-8') as report_file:
        report_file.write("# Progress Report\n")
        report_file.write("## List of all files in the repository\n")
        for file in repo_files:
            report_file.write(f"- {file}\n")

        report_file.write("\n## File Evaluation\n")

        for category, files in categories.items():
            report_file.write(f"\n## {category}\n")
            for file in files:
                file_importance = 'High' if category in ['Server Connection', 'Site Scraper', 'Frontend'] else 'Medium'
                file_comments = 'Optimization needed.' if category == 'Frontend' else 'Review for improvements.'
                report_file.write(f"- {file['path']}: {file['lines']} lines\n")
                report_file.write(f"  - Status: {file['status']}\n")
                report_file.write(f"  - Importance: {file_importance}\n")
                report_file.write(f"  - Comments: {file_comments}\n")

if __name__ == "__main__":
    main()