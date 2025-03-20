import os
import re

def update_brand_link(content):
    # Pattern to match the brand link
    pattern = r'<a href="\./?"'
    replacement = '<a href="./index.html"'
    
    # Replace the link
    return re.sub(pattern, replacement, content)

# Process all HTML files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        print(f"Processing {filename}...")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if the link is already correct
            if 'href="./index.html"' not in content:
                new_content = update_brand_link(content)
                if new_content != content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
                else:
                    print(f"No changes needed in {filename}")
            else:
                print(f"Brand link already correct in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

print("Done updating brand links.") 