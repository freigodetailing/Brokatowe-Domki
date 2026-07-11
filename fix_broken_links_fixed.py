import os
import re

html_path = r"C:\Users\LENOVO\Desktop\Brokatowe Domki Strona Internetowa\Brokatowe-Domki-NOWE\Brokatowe-Domki-main\galeria.html"
base_dir = r"C:\Users\LENOVO\Desktop\Brokatowe Domki Strona Internetowa\Brokatowe-Domki-NOWE\Brokatowe-Domki-main"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Using regex to find gallery items
pattern = r'<div class="u-effect-hover-zoom u-gallery-item[^>]*>.*?<img[^>]+src="([^"]+)".*?</div>\s*</div>\s*</div>'

def replacer(match):
    full_html = match.group(0)
    img_src = match.group(1)
    img_path = os.path.join(base_dir, img_src.replace('/', '\\'))
    if not os.path.exists(img_path):
        print(f"Removing broken image reference: {img_src}")
        return ""
    return full_html

new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Finished checking for broken links.")
