import re
import os

def update_file_content(content):
    # Ensure there are two blank lines after imports
    content = re.sub(r'(import [^\n]+)(\n)(import)', r'\1\n\n\3', content)
    # Ensure there is exactly one blank line after class and function definitions
    content = re.sub(r'(\n\n)(def |class )', r'\n\2', content)
    # Ensure there are no trailing blank lines at the end of the file
    content = re.sub(r'\n+\Z', '\n', content)
    return content

def update_files(file_paths):
    log_entries = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = update_file_content(content)
        
        with open(file_path, 'w') as file:
            file.write(new_content)
        
        log_entry = f'Updated {file_path}'
        log_entries.append(log_entry)
        print(log_entry)
    
    with open('update_log.txt', 'a') as log_file:
        log_file.write('\n'.join(log_entries) + '\n')

if __name__ == "__main__":
    file_paths = [
        'backend/server_connection.py',
        'backend/site_scraper.py',
        'backend/scrape_zillow_with_selenium.py',
        'backend/single_family_evaluation.py',
        'backend/multi_family_evaluation.py',
        'backend/offer_generator.py'
    ]
    update_files(file_paths)