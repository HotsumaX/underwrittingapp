import os
import subprocess

def run_flake8(filepath):
    result = subprocess.run(['flake8', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by flake8."

def run_pylint(filepath):
    result = subprocess.run(['pylint', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by pylint."

def run_bandit(filepath):
    result = subprocess.run(['bandit', '-r', filepath], capture_output=True, text=True)
    return result.stdout if result.stdout else "No issues found by bandit."

def get_file_status(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    return lines

def generate_recommendations(flake8_report, pylint_report, bandit_report, file_status):
    recommendations = []
    if "missing-module-docstring" in pylint_report:
        recommendations.append("Add a module docstring to describe the purpose and functionality of the module.")
    if "line-too-long" in pylint_report or "E501" in flake8_report:
        recommendations.append("Refactor lines to ensure they do not exceed 79 characters.")
    if "missing-timeout" in bandit_report:
        recommendations.append("Add a timeout parameter to all requests to prevent hanging.")
    if "import os" in file_status and "import subprocess" not in file_status:
        recommendations.append("Ensure that subprocess is imported if os is used for executing shell commands.")
    if any("W1514" in line for line in pylint_report):
        recommendations.append("Specify an encoding when using open() to avoid potential issues with different environments.")
    return recommendations

def evaluate_files(filepaths):
    evaluations = {}
    for filepath in filepaths:
        flake8_report = run_flake8(filepath)
        pylint_report = run_pylint(filepath)
        bandit_report = run_bandit(filepath)
        file_status = get_file_status(filepath)
        
        evaluations[filepath] = {
            'flake8': flake8_report,
            'pylint': pylint_report,
            'bandit': bandit_report,
            'status': file_status,
            'recommendations': generate_recommendations(flake8_report, pylint_report, bandit_report, file_status),
        }
    return evaluations

def main():
    repo_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                repo_files.append(os.path.join(root, file))

    evaluations = evaluate_files(repo_files)
    with open('README.md', 'a') as readme:
        readme.write("\n## Detailed File Evaluations\n")
        for filepath, evals in evaluations.items():
            readme.write(f"\n### {filepath}\n")
            for tool, report in evals.items():
                if tool != 'recommendations' and tool != 'status':
                    readme.write(f"#### {tool} Report:\n{report}\n")
            readme.write("#### Recommendations:\n")
            for recommendation in evals['recommendations']:
                readme.write(f"- {recommendation}\n")

if __name__ == "__main__":
    main()