import os
import subprocess
import re
import subprocess
import os

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout if result.stdout else result.stderr

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

    with open('README.md', 'a') as f:
        f.write("\n## Project Analysis Report\n")
        f.write(analysis_report)

if __name__ == '__main__':
    enhance_documentation()
def run_flake8(filepath):
    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by flake8."

def run_pylint(filepath):
    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by pylint."

def run_bandit(filepath):
    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by bandit."

def evaluate_files(filepaths):
    evaluations = []
    for filepath in filepaths:
        if os.path.isdir(filepath):
            continue
        flake8_report = run_flake8(filepath)
        pylint_report = run_pylint(filepath)
        bandit_report = run_bandit(filepath)
        evaluations.append((filepath, flake8_report, pylint_report, bandit_report))
    return evaluations

def summarize_evaluations(evaluations):
    summary = "# Progress Report\n\n"
    for filepath, flake8_report, pylint_report, bandit_report in evaluations:
        summary += f"## {filepath}\n"
        summary += f"### flake8 Report:\n{flake8_report}\n"
        summary += f"### pylint Report:\n{pylint_report}\n"
        summary += f"### bandit Report:\n{bandit_report}\n\n"
    return summary

def main():
    repo_files = [os.path.join(root, file) for root, _, files in os.walk(".") for file in files if file.endswith(".py")]
    evaluations = evaluate_files(repo_files)
    summary = summarize_evaluations(evaluations)

    with open("progress_report.md", "w") as report_file:
        report_file.write(summary)

    # Add summary of next steps
    next_steps = """
## Summary

### Current Status
The following sections outline the current state of the repository based on the evaluation:

 - **Server Connection Improvement**: Improve the reliability and efficiency of the server connection module.
 - **Site Scraper Enhancement**: Ensure robust scraping logic and error handling.
 - **Evaluation of Single Family Homes**: Implement a comprehensive evaluation logic for single-family homes.
 - **Multi-Family Homes Evaluation**: Adapt the single-family evaluation logic to handle multi-family specifics.
 - **Property Offer Generator**: Create a module that generates offers based on evaluated data.

### Next Steps
To align the project with the outlined goals, the following actions are recommended:
- Improve server connection reliability and efficiency.
- Enhance site scraper with better logging and error handling.
- Implement evaluation logic for single-family and multi-family homes.
- Develop the property offer generator module.

"""
    with open("progress_report.md", "a") as report_file:
        report_file.write(next_steps)

if __name__ == "__main__":
    main()