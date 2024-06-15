import os
import subprocess

# List of directories to exclude from the analysis
EXCLUDE_DIRS = ['node_modules', 'venv', '.venv', '__pycache__', 'dist', 'build']

def run_command(command):
    """Executes a shell command and captures the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout if result.stdout else result.stderr
    except subprocess.CalledProcessError as e:
        return e.output if e.output else str(e)

def analyze_file(filepath):
    """Runs static analysis tools on a given file and returns the results."""
    print(f"Analyzing {filepath}...")  # Progress logging
    analysis_results = {}
    if filepath.endswith('.py'):
        analysis_results['flake8'] = run_command(f'flake8 {filepath}')  # Runs flake8 on the file
        analysis_results['pylint'] = run_command(f'pylint {filepath}')  # Runs pylint on the file
        analysis_results['bandit'] = run_command(f'bandit {filepath}')  # Runs bandit on the file
    elif filepath.endswith('.js'):
        # Add JavaScript analysis tools here if needed
        pass
    elif filepath.endswith('.html') or filepath.endswith('.css'):
        # Add HTML/CSS analysis tools here if needed
        pass
    elif filepath.endswith('.json'):
        # Add JSON analysis tools here if needed
        pass
    return analysis_results

def generate_analysis_report(file_analysis):
    """Generates a comprehensive report from the analysis results of all files."""
    report = ''
    for filepath, analysis in file_analysis.items():
        report += f"\n## Analysis of {filepath}\n"
        if 'flake8' in analysis:
            report += "\n### Flake8 Results:\n"
            report += f"{analysis['flake8']}\n"
        if 'pylint' in analysis:
            report += "\n### Pylint Results:\n"
            report += f"{analysis['pylint']}\n"
        if 'bandit' in analysis:
            report += "\n### Bandit Results:\n"
            report += f"{analysis['bandit']}\n"
    return report

def summarize_evaluations(evaluations):
    """Summarizes the analysis results for all evaluated files."""
    summary = "# Progress Report\n\n"
    for filepath, analysis in evaluations.items():
        summary += f"## {filepath}\n"
        if 'flake8' in analysis:
            summary += f"### flake8 Report:\n{analysis['flake8']}\n"
        if 'pylint' in analysis:
            summary += f"### pylint Report:\n{analysis['pylint']}\n"
        if 'bandit' in analysis:
            summary += f"### bandit Report:\n{analysis['bandit']}\n\n"
    return summary

def should_exclude(directory):
    """Checks if a directory should be excluded."""
    for exclude_dir in EXCLUDE_DIRS:
        if exclude_dir in directory:
            return True
    return False

def main():
    """Main function to find all files, run analysis, and generate reports."""
    # Find all files in the repository, excluding specified directories
    repo_files = []
    for root, _, files in os.walk("."):
        if should_exclude(root):
            continue
        for file in files:
            if file.endswith(('.py', '.js', '.html', '.css', '.json')):
                repo_files.append(os.path.join(root, file))

    # Analyze all found files
    evaluations = {file: analyze_file(file) for file in repo_files}

    # Generate a summary report of the analysis
    summary = summarize_evaluations(evaluations)

    # Write the summary report to progress_report.md
    with open("progress_report.md", "w", encoding="utf-8") as report_file:
        report_file.write(summary)

    # Add a section with next steps for improvement
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

    # Append the next steps section to the progress report
    with open("progress_report.md", "a", encoding="utf-8") as report_file:
        report_file.write(next_steps)

if __name__ == "__main__":
    main()