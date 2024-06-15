import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_files(file_patterns):
    log_entries = []
    for pattern in file_patterns:
        file_paths = glob.glob(pattern, recursive=True)
        for file_path in file_paths:
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # Simulating an update (actual update logic will go here)
                    new_content = content  # Update this as per your logic
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    log_entries.append(f"Updated: {file_path}")
                    logger.info(f"Updated: {file_path}")
                except Exception as e:
                    logger.error(f"Failed to update {file_path}: {e}")
                    log_entries.append(f"Failed to update {file_path}: {e}")
            else:
                logger.warning(f"Skipped non-file path: {file_path}")
    return log_entries

def main():
    repo_files = ['backend/*.py', 'frontend/*.js']  # Add all relevant patterns
    log_entries = update_files(repo_files)
    with open('update_log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write("\n".join(log_entries) + "\n")
    logger.info("Update process completed.")

if __name__ == "__main__":
    main()