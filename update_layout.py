import os
import re

def update_layout(content):
    # Add layout-fluid class to body if not present
    if 'class="layout-fluid"' not in content:
        content = content.replace('<body', '<body class="layout-fluid"')
    
    # Replace horizontal navbar with vertical sidebar
    sidebar_template = '''<!-- BEGIN SIDEBAR -->
      <aside class="navbar navbar-vertical navbar-expand-lg" data-bs-theme="dark">
        <div class="container-fluid">
          <!-- BEGIN NAVBAR TOGGLER -->
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#sidebar-menu" aria-controls="sidebar-menu" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <!-- END NAVBAR TOGGLER -->
          <!-- BEGIN NAVBAR LOGO -->
          <div class="navbar-brand navbar-brand-autodark">
            <a href="./index.html">
              Tabler
            </a>
          </div>
          <!-- END NAVBAR LOGO -->
          <div class="navbar-nav flex-row d-lg-none">
            <div class="nav-item d-none d-lg-flex me-3">
              <div class="btn-list">
                <a href="https://github.com/tabler/tabler" class="btn btn-5" target="_blank" rel="noreferrer">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-2">
                    <path d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5" />
                  </svg>
                  Source code
                </a>
              </div>
            </div>
            <div class="d-none d-lg-flex">
              <div class="nav-item">
                <a href="?theme=dark" class="nav-link px-0 hide-theme-dark" title="Enable dark mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1">
                    <path d="M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z" />
                  </svg>
                </a>
                <a href="?theme=light" class="nav-link px-0 hide-theme-light" title="Enable light mode" data-bs-toggle="tooltip" data-bs-placement="bottom">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1">
                    <path d="M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" />
                    <path d="M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7" />
                  </svg>
                </a>
              </div>
            </div>
          </div>
          <!-- BEGIN NAVBAR MENU -->
          <div class="collapse navbar-collapse" id="sidebar-menu">
            <ul class="navbar-nav pt-lg-3">
              <li class="nav-item">
                <a class="nav-link" href="./index.html">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1">
                      <path d="M5 12l-2 0l9 -9l9 9l-2 0" />
                      <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
                      <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6" />
                    </svg>
                  </span>
                  <span class="nav-link-title">Home</span>
                </a>
              </li>
              <li class="nav-item">
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
              </li>
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#navbar-base" data-bs-toggle="dropdown" data-bs-auto-close="outside" role="button" aria-expanded="false">
                  <span class="nav-link-icon d-md-none d-lg-inline-block">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1">
                      <path d="M12 3l8 4.5l0 9l-8 4.5l-8 -4.5l0 -9l8 -4.5" />
                      <path d="M12 12l8 -4.5" />
                      <path d="M12 12l0 9" />
                      <path d="M12 12l-8 -4.5" />
                      <path d="M16 5.25l-8 4.5" />
                    </svg>
                  </span>
                  <span class="nav-link-title">Interface</span>
                </a>
                <div class="dropdown-menu">
                  <div class="dropdown-menu-columns">
                    <div class="dropdown-menu-column">
                      <a class="dropdown-item" href="./accordion.html">Accordion</a>
                      <a class="dropdown-item" href="./alerts.html">Alerts</a>
                      <a class="dropdown-item" href="./badges.html">Badges</a>
                      <a class="dropdown-item" href="./buttons.html">Buttons</a>
                      <a class="dropdown-item" href="./cards.html">Cards</a>
                      <a class="dropdown-item" href="./carousel.html">Carousel</a>
                      <a class="dropdown-item" href="./colors.html">Colors</a>
                      <a class="dropdown-item" href="./datagrid.html">Data grid</a>
                      <a class="dropdown-item" href="./dropdowns.html">Dropdowns</a>
                      <a class="dropdown-item" href="./lists.html">Lists</a>
                      <a class="dropdown-item" href="./modals.html">Modals</a>
                      <a class="dropdown-item" href="./markdown.html">Markdown</a>
                    </div>
                    <div class="dropdown-menu-column">
                      <a class="dropdown-item" href="./navigation.html">Navigation</a>
                      <a class="dropdown-item" href="./offcanvas.html">Offcanvas</a>
                      <a class="dropdown-item" href="./pagination.html">Pagination</a>
                      <a class="dropdown-item" href="./placeholder.html">Placeholder</a>
                      <a class="dropdown-item" href="./segmented-control.html">Segmented control</a>
                      <a class="dropdown-item" href="./scroll-spy.html">Scroll spy</a>
                      <a class="dropdown-item" href="./social-icons.html">Social icons</a>
                      <a class="dropdown-item" href="./stars-rating.html">Stars rating</a>
                      <a class="dropdown-item" href="./steps.html">Steps</a>
                      <a class="dropdown-item" href="./tables.html">Tables</a>
                      <a class="dropdown-item" href="./tabs.html">Tabs</a>
                      <a class="dropdown-item" href="./tags.html">Tags</a>
                      <a class="dropdown-item" href="./toasts.html">Toasts</a>
                      <a class="dropdown-item" href="./typography.html">Typography</a>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
          <!-- END NAVBAR MENU -->
        </div>
      </aside>
      <!-- END SIDEBAR -->'''

    # Replace container-xl with container-fluid
    content = content.replace('container-xl', 'container-fluid')
    
    # Find and replace the old navbar structure
    # First try to find the navbar section
    navbar_pattern = r'<!-- Navbar -->.*?<!-- END NAVBAR MENU -->'
    if re.search(navbar_pattern, content, re.DOTALL):
        content = re.sub(navbar_pattern, sidebar_template, content, flags=re.DOTALL)
    else:
        # If no navbar section found, try to find the header section
        header_pattern = r'<header.*?class="navbar.*?">.*?</header>'
        content = re.sub(header_pattern, sidebar_template, content, flags=re.DOTALL)
    
    return content

# Process all HTML files
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        print(f"Processing {filename}...")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already using fluid layout
            if 'class="layout-fluid"' in content and 'navbar-vertical' in content:
                print(f"Already using fluid layout in {filename}")
                continue
                
            new_content = update_layout(content)
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                print(f"No changes needed in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

print("Done updating layouts.") 