import os
from bs4 import BeautifulSoup

def get_nav_order(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Helper to extract text from nav
        def extract_nav_items(nav_class):
            nav = soup.find('ul', class_=nav_class)
            if not nav:
                return []
            items = []
            for li in nav.find_all('li', class_='u-nav-item'):
                a = li.find('a')
                if a:
                    text = a.get_text(strip=True)
                    # Filter out empty or invisible items if any
                    if text:
                        items.append(text)
            return items

        # Usually u-nav-1 is the desktop menu
        desktop_items = extract_nav_items('u-nav-1')
        
        return desktop_items

    except Exception as e:
        return [f"Error: {e}"]

root_dir = os.getcwd()
files_to_check = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith('.html') and 'backup' not in file.lower():
            files_to_check.append(os.path.join(root, file))

print("Checking Navigation Order...")
for filepath in sorted(files_to_check):
    items = get_nav_order(filepath)
    rel_path = os.path.relpath(filepath, root_dir)
    print(f"{rel_path}: {items}")
