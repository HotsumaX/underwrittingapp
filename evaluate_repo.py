import os

def get_file_status(filepath):
    if os.path.isdir(filepath):
        return 'Directory'
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            if content.strip():
                return 'Has content'
            else:
                return 'Empty'
    except Exception as e:
        return str(e)

def list_files_and_status(directory):
    files_status = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            status = get_file_status(filepath)
            files_status.append((filepath, status))
    return files_status

def update_readme(files_status):
    with open('README.md', 'r') as readme_file:
        readme_content = readme_file.read()

    start_marker = '<!-- PROGRESS_REPORT_START -->'
    end_marker = '<!-- PROGRESS_REPORT_END -->'

    if start_marker in readme_content and end_marker in readme_content:
        before_content = readme_content.split(start_marker)[0]
        after_content = readme_content.split(end_marker)[1]
    else:
        before_content = readme_content
        after_content = ''

    new_report = f"{start_marker}\n## Progress Report\n\n"
    for filepath, status in files_status:
        new_report += f"- {filepath}: {status}\n"
    new_report += f"\n{end_marker}"

    new_readme_content = before_content + new_report + after_content

    with open('README.md', 'w') as readme_file:
        readme_file.write(new_readme_content)

def main():
    files_status = list_files_and_status('.')
    update_readme(files_status)

if __name__ == '__main__':
    main()