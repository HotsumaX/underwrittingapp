import os
import re
import subprocess

def run_command(command):
    """Run a command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout if result.stdout else result.stderr
    except subprocess.CalledProcessError as e:
        return e.output if e.output else e.stderr

def update_file_content(content):
    """Update the content of a file based on certain rules."""
    # Ensure blank line between import groups
    content = re.sub(r'(\nimport .+)(\nimport .+)', r'\1\n\2', content)
    # Ensure two blank lines before class or function definitions
    content = re.sub(r'\n+(def|class) ', r'\n\n\1 ', content)
    return content

def update_files(file_paths):
    """Update and audit a list of files."""
    log_lines = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        new_content = update_file_content(content)

        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            log_lines.append(f"Updated {file_path}")

        # Check if the content is correct
        if content == new_content:
            log_lines.append(f"{file_path} content is correct")
        else:
            log_lines.append(f"{file_path} content is incorrect")

    # Write the log to update_log.txt
    with open('update_log.txt', 'w', encoding='utf-8') as log_file:
        log_file.write('\n'.join(log_lines))

def analyze_file(filepath):
    """Analyze a file using flake8, pylint, and bandit."""
    analysis_results = {
        'flake8': run_command(f'flake8 {filepath}'),
        'pylint': run_command(f'pylint {filepath}'),
        'bandit': run_command(f'bandit -r {filepath}')
    }
    return analysis_results

def generate_analysis_report(file_analysis):
    """Generate a report based on the analysis results."""
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
    """Enhance the project documentation."""
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
    """Main function to update files and generate the progress report."""
    repo_files = [
        'backend/server_connection.py', 'backend/site_scraper.py',
        'backend/scrape_zillow_with_selenium.py', 'backend/single_family_evaluation.py',
        'backend/multi_family_evaluation.py', 'backend/offer_generator.py'
    ]

    update_files(repo_files)
    
    # Generate the progress report
    evaluations = {}
    for filepath in repo_files:
        evaluations[filepath] = analyze_file(filepath)
        
    summary = generate_analysis_report(evaluations)

    with open("progress_report.md", "w", encoding="utf-8") as report_file:
        report_file.write(summary)

    # Append the current state summary and next steps
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
    with open("progress_report.md", "a", encoding="utf-8") as report_file:
        report_file.write(next_steps)

if __name__ == "__main__":
    main()