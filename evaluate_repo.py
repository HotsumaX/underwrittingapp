import os

def list_files_in_repo():
    repo_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') or file.endswith('.js') or file.endswith('.json'):
                repo_files.append(os.path.join(root, file))
    return repo_files

def get_file_status(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        if len(content) == 0:
            return 'exists but is empty'
        else:
            return 'exists and has content'
    except FileNotFoundError:
        return 'does not exist'
    except IsADirectoryError:
        return 'is a directory'

def evaluate_code(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        lines = content.split('\n')
        functions = [line for line in lines if line.strip().startswith('def ')]
        classes = [line for line in lines if line.strip().startswith('class ')]
        imports = [line for line in lines if line.strip().startswith('import ') or line.strip().startswith('from ')]
        return {
            'functions': functions,
            'classes': classes,
            'imports': imports,
            'lines_of_code': len(lines)
        }
    except Exception as e:
        return str(e)

def evaluate_files(filepaths):
    report = []
    for filepath in filepaths:
        status = get_file_status(filepath)
        if status == 'exists and has content':
            code_evaluation = evaluate_code(filepath)
            report.append(f'- {filepath} {status}.')
            report.append(f'  - Lines of code: {code_evaluation["lines_of_code"]}')
            report.append(f'  - Functions: {len(code_evaluation["functions"])}')
            report.append(f'  - Classes: {len(code_evaluation["classes"])}')
            report.append(f'  - Imports: {len(code_evaluation["imports"])}')
        else:
            report.append(f'- {filepath} {status}.')
    return report

def main():
    repo_files = list_files_in_repo()
    with open('progress_report.md', 'w') as report_file:
        report_file.write('# Progress Report\n\n')
        
        # List all files in the repository
        report_file.write('## List of all files in the repository\n\n')
        for repo_file in repo_files:
            report_file.write(f'- {repo_file}\n')
        report_file.write('\n')
        
        # Evaluate files for each section
        sections = {
            'Server Connection': ['backend/server_connection.py'],
            'Site Scraper': ['backend/site_scraper.py'],
            'Single Family Evaluation': ['backend/single_family_evaluation.py'],
            'Multi Family Evaluation': ['backend/multi_family_evaluation.py'],
            'Email Contact': ['backend/email_contact.py'],
            'Property Management': ['backend/property_management.py'],
            'Log Section': ['backend/log_section.py'],
            'Offer Generator': ['backend/offer_generator.py'],
            'Frontend': [os.path.join(root, file) for root, dirs, files in os.walk('frontend/src') for file in files]
        }
        
        for section, files in sections.items():
            report_file.write(f'## {section}\n\n')
            evaluation = evaluate_files(files)
            for line in evaluation:
                report_file.write(f'{line}\n')
            report_file.write('\n')

if __name__ == '__main__':
    main()