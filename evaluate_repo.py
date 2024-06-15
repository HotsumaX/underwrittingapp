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

def read_outline(filepath):
    """Reads the application outline from a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def update_outline(filepath, new_content):
    """Updates the application outline with new content."""
    with open(filepath, 'a', encoding='utf-8') as file:
        file.write(new_content)

def generate_next_steps(evaluations):
    """Generates next steps based on the analysis results."""
    steps = ["## Summary\n", "### Current Status\n", "The following sections outline the current state of the repository based on the evaluation:\n"]

    flake8_issues = 0
    pylint_issues = 0
    bandit_issues = 0

    for analysis in evaluations.values():
        if 'flake8' in analysis and analysis['flake8']:
            flake8_issues += analysis['flake8'].count('\n')
        if 'pylint' in analysis and analysis['pylint']:
            pylint_issues += analysis['pylint'].count('\n')
        if 'bandit' in analysis and analysis['bandit']:
            bandit_issues += analysis['bandit'].count('\n')

    # Add recommendations based on the count of issues found
    if flake8_issues > 0:
        steps.append(f" - **Code Style Improvement**: Address the {flake8_issues} issues reported by flake8.\n")
    if pylint_issues > 0:
        steps.append(f" - **Code Quality Enhancement**: Resolve the {pylint_issues} warnings and errors reported by pylint.\n")
    if bandit_issues > 0:
        steps.append(f" - **Security Improvement**: Fix the {bandit_issues} security issues identified by bandit.\n")

    # Add general next steps
    steps.append("\n### Next Steps\nTo align the project with the outlined goals, the following actions are recommended:\n")
    if flake8_issues > 0:
        steps.append("- Improve code style and consistency by addressing flake8 issues.\n")
    if pylint_issues > 0:
        steps.append("- Enhance code quality by resolving pylint warnings and errors.\n")
    if bandit_issues > 0:
        steps.append("- Improve security by fixing issues identified by bandit.\n")
    
    steps.append("- Improve server connection reliability and efficiency.\n")
    steps.append("- Enhance site scraper with better logging and error handling.\n")
    steps.append("- Implement evaluation logic for single-family and multi-family homes.\n")
    steps.append("- Develop the property offer generator module.\n")
    
    return "".join(steps)

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

    # Read the existing application outline
    outline_path = 'appoutline.txt'
    outline = read_outline(outline_path)

    # Append the analysis summary to the application outline
    updated_outline = outline + "\n" + summary
    update_outline(outline_path, "\n" + summary)

    # Generate next steps based on the evaluations
    next_steps = generate_next_steps(evaluations)

    # Write the summary report and next steps to progress_report.md
    with open("progress_report.md", "w", encoding="utf-8") as report_file:
        report_file.write(summary)
        report_file.write(next_steps)

if __name__ == "__main__":
    main()