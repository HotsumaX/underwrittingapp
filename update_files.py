import os
import re
import subprocess
import datetime

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    return result.stdout if result.stdout else result.stderr

def update_file_content(content):
    # Ensure blank line between import groups
    content = re.sub(r'(?<=\bimport\b[^\n]*\n)(?=\bimport\b)', '\n', content)
    # Add blank line before class and def definitions if not present
    content = re.sub(r'(?<!\n)\n(class|def) ', r'\n\n\1 ', content)
    # Ensure function docstrings are present
    content = re.sub(r'(?<=def [^\n]+:\n)(\s*)(?!\"\"\")', r'\1    """Function docstring"""\n\1    ', content)
    return content

def analyze_file(filepath):
    analysis_results = {
        'flake8': run_command(f'flake8 {filepath}'),
        'pylint': run_command(f'pylint {filepath}'),
        'bandit': run_command(f'bandit -r {filepath}')
    }
    return analysis_results

def update_files(file_paths):
    log_entries = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = update_file_content(content)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)

        log_entries.append(f"Updated {file_path}")

        analysis_results = analyze_file(file_path)
        log_entries.append(f"Analysis for {file_path}:")
        for tool, result in analysis_results.items():
            log_entries.append(f"{tool}: {result}")

    return log_entries

def main():
    repo_files = [
        'backend/server_connection.py',
        'backend/site_scraper.py',
        'backend/scrape_zillow_with_selenium.py',
        'backend/single_family_evaluation.py',
        'backend/multi_family_evaluation.py',
        'backend/offer_generator.py'
    ]

    log_entries = update_files(repo_files)

    with open('update_log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(f"\nUpdate log - {datetime.datetime.now()}:\n")
        log_file.write('\n'.join(log_entries) + '\n')

if __name__ == "__main__":
    main()