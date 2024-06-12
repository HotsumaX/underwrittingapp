import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def get_file_status(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as file:
            content = file.read()
        return content
    except Exception as e:
        return str(e)

def run_tool(tool, filepath):
    result = subprocess.run([tool, filepath], capture_output=True, text=True)
    return result.stdout.strip()

def generate_comments(filepath):
    flake8_comments = run_tool("flake8", filepath)
    pylint_comments = run_tool("pylint", filepath)
    bandit_comments = run_tool("bandit", filepath)
    comments = f"### Flake8 Comments:\n{flake8_comments}\n\n### Pylint Comments:\n{pylint_comments}\n\n### Bandit Comments:\n{bandit_comments}"
    return comments

def evaluate_files(filepaths):
    evaluations = []
    for filepath in filepaths:
        status = get_file_status(filepath)
        comments = generate_comments(filepath) if "Error reading file" not in status else status
        evaluations.append({
            'filepath': filepath,
            'status': status,
            'comments': comments
        })
    return evaluations

def list_files(directory):
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames]

def main():
    repo_files = list_files('.')
    evaluations = evaluate_files(repo_files)
    
    with open('progress_report.md', 'w') as report:
        report.write("# Progress Report\n\n")
        report.write("## List of all files in the repository\n")
        for filepath in repo_files:
            report.write(f"- {filepath}\n")
        report.write("\n## File Evaluation\n")
        for evaluation in evaluations:
            report.write(f"\n### {evaluation['filepath']}\n")
            report.write(f"- Status: {evaluation['status']}\n")
            report.write(f"- Comments: {evaluation['comments']}\n")

if __name__ == "__main__":
    main()