import os
import subprocess

def list_files_in_directory(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):  # Only consider Python files
                filepath = os.path.join(root, filename)
                files.append(filepath)
    return files

def run_flake8(filepath):
    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by flake8."

def run_pylint(filepath):
    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by pylint."

def run_bandit(filepath):
    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by bandit."

def evaluate_files(files):
    evaluations = {}
    for filepath in files:
        flake8_report = run_flake8(filepath)
        pylint_report = run_pylint(filepath)
        bandit_report = run_bandit(filepath)
        
        evaluations[filepath] = {
            'flake8': flake8_report,
            'pylint': pylint_report,
            'bandit': bandit_report,
        }
    return evaluations

def main():
    repo_files = list_files_in_directory('.')
    app_outline = ''
    
    with open('appoutline.txt', 'r', encoding='utf-8') as file:
        app_outline = file.read()
    
    progress_report = "# Progress Report\n\n## Repository Files\n"
    
    for filepath in repo_files:
        file_evaluation = evaluate_files([filepath])
        progress_report += f"\n### {filepath}\n"
        progress_report += "#### flake8 Report:\n"
        progress_report += file_evaluation[filepath]['flake8'] + "\n"
        progress_report += "#### pylint Report:\n"
        progress_report += file_evaluation[filepath]['pylint'] + "\n"
        progress_report += "#### bandit Report:\n"
        progress_report += file_evaluation[filepath]['bandit'] + "\n"

    with open('progress_report.md', 'w', encoding='utf-8') as report_file:
        report_file.write(progress_report)

if __name__ == "__main__":
    main()