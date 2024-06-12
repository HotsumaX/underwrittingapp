import os
import openai

# Ensure you have your OpenAI API key set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

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

def read_app_outline(filepath="appoutline.txt"):
    with open(filepath, 'r') as file:
        app_outline = file.read()
    return app_outline

def generate_comments(filepath, lines, app_outline):
    if isinstance(lines, str):
        return lines
    
    file_content = ''.join(lines)
    prompt = f"Evaluate the following code file and provide detailed comments, suggestions for improvements, and how to align it with the given app outline. App outline: {app_outline}\n\nFile content:\n{file_content}"
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        comments = response.choices[0].text.strip()
    except Exception as e:
        comments = f"Error generating comments: {str(e)}"
    
    return comments

def evaluate_files(files, app_outline):
    evaluations = []
    for filepath in files:
        lines = get_file_status(filepath)
        if isinstance(lines, str):
            status = f"Error reading file: {lines}"
            importance = "Medium"
        else:
            status = "File read successfully."
            importance = "High" if "backend" in filepath or "frontend" in filepath else "Medium"
        
        comments = generate_comments(filepath, lines, app_outline)
        evaluations.append({
            "path": filepath,
            "status": status,
            "importance": importance,
            "comments": comments
        })
    return evaluations

def list_repo_files(root_dir="."):
    repo_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if ".git" not in filepath and not filepath.endswith(".pyc"):
                repo_files.append(filepath)
    return repo_files

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

def main():
    app_outline = read_app_outline()
    repo_files = list_repo_files()
    evaluations = evaluate_files(repo_files, app_outline)
    progress_report = generate_progress_report(evaluations)

    with open("progress_report.md", "w") as report_file:
        report_file.write(progress_report)

    with open("README.md", "a") as readme_file:
        readme_file.write(progress_report)

if __name__ == "__main__":
    main()