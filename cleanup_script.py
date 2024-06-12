import os

def find_empty_files(directory):
    empty_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0:
                empty_files.append(file_path)
    return empty_files

def remove_empty_files(directory):
    empty_files = find_empty_files(directory)
    for file in empty_files:
        os.remove(file)
        print(f"Removed: {file}")

def main():
    remove_empty_files('.')

if __name__ == "__main__":
    main()

