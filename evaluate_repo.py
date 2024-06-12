import os

# Define the outline for comparison
outline = {
    "1. Server Connection Status": [
        "server connection status display",
        "server connection reset button",
        "sample payload fetch button",
        "success/failure indicators"
    ],
    "2. Site Scraper": [
        "listing scraper for CREXi",
        "listing scraper for Zillow",
        "backend storage for scraped data",
        "data querying functionality"
    ],
    # Add other sections as needed...
}

def check_progress(directory, outline):
    progress_report = {}
    
    for section, tasks in outline.items():
        progress_report[section] = {task: False for task in tasks}
    
    # Walk through the directory and check for task completion
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for section, tasks in outline.items():
                    for task in tasks:
                        if task in content:
                            progress_report[section][task] = True
    
    return progress_report

def generate_report(progress_report):
    report = []
    for section, tasks in progress_report.items():
        report.append(f"## {section}\n")
        for task, completed in tasks.items():
            status = "Completed" if completed else "Pending"
            report.append(f"- {task}: {status}\n")
        report.append("\n")
    
    with open("progress_report.md", "w") as f:
        f.writelines(report)

if __name__ == "__main__":
    directory = "."
    progress_report = check_progress(directory, outline)
    generate_report(progress_report)
    print("Progress report generated in progress_report.md")