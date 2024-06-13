import re
import os
import subprocess

def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout if result.returncode == 0 else result.stderr

def update_file_content(content):
    """Update the content of a file with required changes."""
    # Ensure blank line between import groups
    content = re.sub(r'(\nimport .+)', r'\1\n', content)
    return content

def update_files(file_paths):
    """Update the contents of files and return log entries."""
    log_entries = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = update_file_content(content)

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            log_entries.append(f"Updated {file_path}")
        else:
            log_entries.append(f"No change for {file_path}")
    
    return log_entries

def analyze_file(filepath):
    """Analyze a file using various tools and return the results."""
    analysis_results = {
        'flake8': run_command(f'flake8 {filepath}'),
        'pylint': run_command(f'pylint {filepath}'),
        'bandit': run_command(f'bandit -r {filepath}')
    }
    return analysis_results

def log_to_file(log_entries, log_file_path):
    """Log entries to a log file."""
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        for entry in log_entries:
            log_file.write(entry + '\n')

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

    for file_path in repo_files:
        if os.path.exists(file_path):
            analysis_results = analyze_file(file_path)
            log_entries.append(f"\nAnalysis for {file_path}:")
            log_entries.append(f"flake8: {analysis_results['flake8']}")
            log_entries.append(f"pylint: {analysis_results['pylint']}")
            log_entries.append(f"bandit: {analysis_results['bandit']}")

    log_to_file(log_entries, 'update_log.txt')

if __name__ == "__main__":
    main()