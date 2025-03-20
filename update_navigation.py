import os
import re

def insert_ubersicht_menu(content):
    # The Übersicht menu item HTML
    ubersicht_menu = '''                      <li class="nav-item">
                        <a class="nav-link" href="./ubersicht.html">
                          <span class="nav-link-icon d-md-none d-lg-inline-block">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                              <path d="M12 13m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0" />
                              <path d="M13.45 11.55l2.05 -2.05" />
                              <path d="M6.4 20a9 9 0 1 1 11.2 0z" />
                            </svg>
                          </span>
                          <span class="nav-link-title">Übersicht</span>
                        </a>
                      </li>'''
    
    # Find the position after the Home menu item and before the Interface dropdown
    home_pattern = r'<span class="nav-link-title">\s*Home\s*</span>\s*</a>\s*</li>'
    match = re.search(home_pattern, content)
    
    if match:
        insert_pos = match.end()
        return content[:insert_pos] + '\n' + ubersicht_menu + content[insert_pos:]
    return content

# Process all HTML files
for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'ubersicht.html':
        print(f"Processing {filename}...")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if Übersicht is already in the file
            if 'Übersicht' not in content:
                new_content = insert_ubersicht_menu(content)
                if new_content != content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
                else:
                    print(f"No changes needed in {filename}")
            else:
                print(f"Übersicht already exists in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

print("Done updating navigation menus.") 