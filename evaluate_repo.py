import os

def get_file_status(filepath):
    if os.path.isdir(filepath):
        return "directory"
    with open(filepath, 'r') as file:
        lines = file.readlines()
        size = len(lines)
        return f"{size} lines"

def evaluate_files(filepaths):
    evaluation = {}
    for filepath in filepaths:
        status = get_file_status(filepath)
        evaluation[filepath] = status
    return evaluation

def main():
    repo_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            repo_files.append(os.path.join(root, file))

    with open('progress_report.md', 'w') as report:
        report.write("# Progress Report\n\n")
        report.write("## List of all files in the repository\n\n")
        for file in repo_files:
            report.write(f"- {file}\n")

        report.write("\n## File Evaluation\n\n")
        evaluations = evaluate_files(repo_files)
        for filepath, status in evaluations.items():
            report.write(f"- {filepath}: {status}\n")

if __name__ == "__main__":
    main()