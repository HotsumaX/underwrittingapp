import re
import os
import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout if result.stdout else result.stderr

def update_file_content(content):
    # Ensure blank line between import groups
    content = re.sub(r'(?<=\bimport\b[^\n]*\n)(?=\bimport\b)', '\n', content)
    return content

def update_files(file_paths):
    log_entries = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        new_content = update_file_content(content)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        log_entries.append(f"Updated {file_path}")
        log_entries.append(f"{file_path} content is correct")
    return log_entries

def analyze_file(filepath):
    analysis_results = {
        'flake8': run_command(f'flake8 {filepath}'),
        'pylint': run_command(f'pylint {filepath}'),
        'bandit': run_command(f'bandit -r {filepath}')
    }
    return analysis_results

def generate_analysis_report(file_analysis):
    report = ''
    for filepath, analysis in file_analysis.items():
        report += f"\n## Analysis of {filepath}\n"
        report += "\n### Flake8 Results:\n"
        report += f"{analysis['flake8']}\n"
        report += "\n### Pylint Results:\n"
        report += f"{analysis['pylint']}\n"
        report += "\n### Bandit Results:\n"
        report += f"{analysis['bandit']}\n"
    return report

def enhance_documentation():
    repo_files = [
        'backend/server_connection.py', 'backend/site_scraper.py', 
        'backend/scrape_zillow_with_selenium.py', 'backend/single_family_evaluation.py', 
        'backend/multi_family_evaluation.py', 'backend/offer_generator.py'
    ]

    file_analysis = {}
    for filepath in repo_files:
        if os.path.exists(filepath):
            file_analysis[filepath] = analyze_file(filepath)
    
    analysis_report = generate_analysis_report(file_analysis)

    with open('README.md', 'a', encoding="utf-8") as f:
        f.write("\n## Project Analysis Report\n")
        f.write(analysis_report)

def main():
    repo_files = [
        'backend/server_connection.py', 'backend/site_scraper.py', 
        'backend/scrape_zillow_with_selenium.py', 'backend/single_family_evaluation.py', 
        'backend/multi_family_evaluation.py', 'backend/offer_generator.py'
    ]
    
    log_entries = update_files(repo_files)
    with open('update_log.txt', 'a', encoding='utf-8') as log_file:
        for entry in log_entries:
            log_file.write(f"{entry}\n")
    
    enhance_documentation()

if __name__ == '__main__':
    main()