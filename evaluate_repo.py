import os

def get_file_status(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        return str(e)

def categorize_file(filepath):
    categories = {
        "server_connection": ["server_connection.py"],
        "site_scraper": ["site_scraper.py", "scrape_crexi.py", "scrape_zillow.py", "scrape_zillow_with_langchain.py", "scrape_zillow_with_selenium.py"],
        "single_family_evaluation": ["single_family_evaluation.py"],
        "multi_family_evaluation": ["multi_family_evaluation.py"],
        "email_contact": ["email_contact.py"],
        "property_management": ["property_management.py"],
        "log_section": ["log_section.py", "app.log"],
        "offer_generator": ["offer_generator.py"],
        "frontend": ["frontend/"],
        "miscellaneous": []
    }
    for category, files in categories.items():
        if any(file in filepath for file in files):
            return category
    return "miscellaneous"

def evaluate_files(files):
    evaluations = []
    for filepath in files:
        lines = get_file_status(filepath)
        if isinstance(lines, str):
            status = f"Error reading file: {lines}"
            importance = "Medium"
        else:
            status = "File read successfully."
            importance = "High" if "backend" in filepath or "frontend" in filepath else "Medium"
        
        comments = generate_comments(filepath, lines)
        evaluations.append({
            "path": filepath,
            "status": status,
            "importance": importance,
            "comments": comments
        })
    return evaluations

def generate_comments(filepath, lines):
    comments = ""
    if isinstance(lines, list):
        line_count = len(lines)
        comments = f"The file contains {line_count} lines.\n"
        
        if line_count == 0:
            comments += "The file is empty and might need implementation or can be removed if not needed."
        else:
            if "import" in lines[0]:
                comments += "File starts with import statements, indicating it might be a script or module.\n"
            if "TODO" in ''.join(lines):
                comments += "The file contains TODO comments that need attention.\n"
            comments += "Review the file for potential improvements, optimizations, or necessary implementations."
    else:
        comments = f"Error encountered: {lines}"
    return comments

def list_repo_files(root_dir="."):
    repo_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if ".git" not in filepath and not filepath.endswith(".pyc"):
                repo_files.append(filepath)
    return repo_files

def main():
    repo_files = list_repo_files()
    evaluations = evaluate_files(repo_files)
    progress_report = generate_progress_report(evaluations)

    with open("progress_report.md", "w") as report_file:
        report_file.write(progress_report)

    with open("README.md", "a") as readme_file:
        readme_file.write(progress_report)

def generate_progress_report(evaluations):
    report = "# Progress Report\n"
    report += "## List of all files in the repository\n"
    for evaluation in evaluations:
        report += f"- {evaluation['path']}\n"
    report += "\n## File Evaluation\n"
    
    categorized_evaluations = {}
    for evaluation in evaluations:
        category = categorize_file(evaluation["path"])
        if category not in categorized_evaluations:
            categorized_evaluations[category] = []
        categorized_evaluations[category].append(evaluation)
    
    for category, evals in categorized_evaluations.items():
        report += f"\n## {category.replace('_', ' ').title()}\n"
        for evaluation in evals:
            report += f"- {evaluation['path']}: {len(evaluation['comments'])} lines\n"
            report += f"  - Status: {evaluation['status']}\n"
            report += f"  - Importance: {evaluation['importance']}\n"
            report += f"  - Comments: {evaluation['comments']}\n"
    return report

if __name__ == "__main__":
    main()