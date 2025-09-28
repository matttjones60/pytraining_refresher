import os
import shutil
import argparse

CONCEPTS = {
    'loops_and_conditions': ['for ', 'while ', 'if ', 'elif ', 'else'],
    'functions_and_modules': ['def ', 'import ', 'from ', 'lambda'],
    'data_structures': ['dict', 'list', 'set', 'tuple'],
    'file_handling': ['open(', 'read(', 'write(', 'with open'],
    'classes_and_oop': ['class ', '__init__', 'self'],
    'learning_misc': []
}

SOURCE_DIR = './your_python_files'  # Update this path

def categorize_by_concept(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            for category, keywords in CONCEPTS.items():
                if any(keyword in content for keyword in keywords):
                    return category
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return 'learning_misc'

def organize_files(dry_run=False):
    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith('.py'):
            full_path = os.path.join(SOURCE_DIR, filename)
            category = categorize_by_concept(full_path)
            target_dir = os.path.join(SOURCE_DIR, category)
            target_path = os.path.join(target_dir, filename)

            if dry_run:
                print(f"[DRY-RUN] Would move {filename} to {category}/")
            else:
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(full_path, target_path)
                print(f"Moved {filename} to {category}/")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Organize Python files by concept.")
    parser.add_argument('--dry-run', action='store_true', help="Preview actions without moving files")
    args = parser.parse_args()

    organize_files(dry_run=args.dry_run)
