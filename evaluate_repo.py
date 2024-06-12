import os

def list_files(startpath):
    file_list = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def categorize_files(file_list):
    categories = {
        "Server Connection": [],
        "Site Scraper": [],
        "Single Family Evaluation": [],
        "Multi Family Evaluation": [],
        "Email Contact": [],
        "Property Management": [],
        "Log Section": [],
        "Offer Generator": [],
        "Frontend": [],
        "Miscellaneous": [],
    }

    for file in file_list:
        if "server_connection" in file:
            categories["Server Connection"].append(file)
        elif "site_scraper" in file or "scrape" in file:
            categories["Site Scraper"].append(file)
        elif "single_family" in file:
            categories["Single Family Evaluation"].append(file)
        elif "multi_family" in file:
            categories["Multi Family Evaluation"].append(file)
        elif "email" in file:
            categories["Email Contact"].append(file)
        elif "property_management" in file:
            categories["Property Management"].append(file)
        elif "log" in file:
            categories["Log Section"].append(file)
        elif "offer_generator" in file:
            categories["Offer Generator"].append(file)
        elif "frontend" in file:
            categories["Frontend"].append(file)
        else:
            categories["Miscellaneous"].append(file)

    return categories

def get_file_status(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return f"{len(lines)} lines"
    except Exception as e:
        return f"Error reading file: {e}"

def evaluate_files(file_list):
    evaluations = []
    for filepath in file_list:
        status = get_file_status(filepath)
        evaluations.append(f"- {filepath}: {status}")
    return evaluations

def main():
    repo_files = list_files(".")
    categories = categorize_files(repo_files)
    evaluations = []

    for category, files in categories.items():
        evaluations.append(f"## {category}\n")
        evaluations.extend(evaluate_files(files))
        evaluations.append("\n")

    with open("progress_report.md", "w") as report:
        report.write("# Progress Report\n\n")
        report.write("## List of all files in the repository\n\n")
        for file in repo_files:
            report.write(f"- {file}\n")
        report.write("\n")
        report.write("## File Evaluation\n\n")
        report.write("\n".join(evaluations))

if __name__ == "__main__":
    main()