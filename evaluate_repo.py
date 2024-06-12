import os
import subprocess
import re

def get_file_status(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return len(lines), "No issues found"

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
        if os.path.isfile(filepath):
            lines, status = get_file_status(filepath)
            flake8_report = run_flake8(filepath)
            pylint_report = run_pylint(filepath)
            bandit_report = run_bandit(filepath)
            evaluations[filepath] = {
                "lines": lines,
                "flake8": flake8_report,
                "pylint": pylint_report,
                "bandit": bandit_report
            }
    return evaluations

def get_repo_files(root_dir):
    repo_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                repo_files.append(os.path.join(dirpath, filename))
    return repo_files

def main():
    repo_files = get_repo_files(".")
    evaluations = evaluate_files(repo_files)

    with open("progress_report.md", "w") as report_file:
        report_file.write("# Progress Report\n\n")
        report_file.write("## Repository Files\n\n")
        for filepath, reports in evaluations.items():
            report_file.write(f"### {filepath}\n")
            report_file.write(f"#### flake8 Report:\n{reports['flake8']}\n")
            report_file.write(f"#### pylint Report:\n{reports['pylint']}\n")
            report_file.write(f"#### bandit Report:\n{reports['bandit']}\n")
            report_file.write("\n")

    with open("appoutline.txt", "r") as app_outline:
        app_outline_content = app_outline.read()

    with open("progress_report.md", "a") as report_file:
        report_file.write("\n## Summary\n\n")
        report_file.write("### Current Status\n")
        report_file.write("The following sections outline the current state of the repository based on the evaluation:\n\n")
        for filepath, reports in evaluations.items():
            status_line = f" - **{filepath}**: {reports['lines']} lines"
            if "No issues found" not in reports["flake8"]:
                status_line += ", has flake8 issues"
            if "No issues found" not in reports["pylint"]:
                status_line += ", has pylint issues"
            if "No issues found" not in reports["bandit"]:
                status_line += ", has bandit issues"
            report_file.write(f"{status_line}\n")

        report_file.write("\n### Next Steps\n")
        report_file.write("To align the project with the outlined goals, the following actions are recommended:\n")
        for section in re.findall(r'## .*?\n', app_outline_content):
            report_file.write(f"- {section.strip()}\n")
        report_file.write("\n")

    with open("README.md", "a") as readme_file:
        readme_file.write("\n")
        with open("progress_report.md", "r") as report_file:
            readme_file.write(report_file.read())

if __name__ == "__main__":
    main()