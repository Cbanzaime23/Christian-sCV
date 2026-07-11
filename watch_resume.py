import os
import time
import subprocess
import sys

# Paths
HTML_FILE = "resume.html"
PDF_FILE = "resume.pdf"

# Find Chrome Executable
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

chrome_path = None
for path in CHROME_PATHS:
    if os.path.exists(path):
        chrome_path = path
        break

if not chrome_path:
    print("Error: Google Chrome was not found in standard installation paths.")
    print("Please install Google Chrome or update the chrome_path in this script.")
    sys.exit(1)

def compile_pdf():
    print(f"[{time.strftime('%H:%M:%S')}] Change detected in {HTML_FILE}. Compiling to {PDF_FILE}...")
    
    # Get absolute paths in URL format for Chrome
    abs_html = os.path.abspath(HTML_FILE)
    abs_pdf = os.path.abspath(PDF_FILE)
    
    # Run Chrome in headless mode to print to PDF
    # --headless=new is the modern headless flag in Chrome
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_pdf}",
        f"file:///{abs_html}"
    ]
    
    try:
        # Run process
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0 or os.path.exists(abs_pdf):
            print(f"[{time.strftime('%H:%M:%S')}] Successfully updated {PDF_FILE}!")
        else:
            print(f"Error during compilation. Return code: {result.returncode}")
            print(f"Stdout: {result.stdout}")
            print(f"Stderr: {result.stderr}")
    except Exception as e:
        print(f"Exception raised while running Chrome: {e}")

def main():
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found in the current directory.")
        sys.exit(1)

    print("=" * 60)
    print(f"Watching {HTML_FILE} in {os.path.abspath('.')}")
    print(f"Using Chrome: {chrome_path}")
    print("Press Ctrl+C to stop watching.")
    print("=" * 60)
    
    # Initial compilation
    compile_pdf()
    
    last_mtime = os.path.getmtime(HTML_FILE)
    
    try:
        while True:
            time.sleep(1)
            # Check if file still exists (it might be temporarily deleted/written during edits)
            if os.path.exists(HTML_FILE):
                current_mtime = os.path.getmtime(HTML_FILE)
                if current_mtime != last_mtime:
                    # Debounce slightly to ensure file write is finished
                    time.sleep(0.5)
                    compile_pdf()
                    last_mtime = os.path.getmtime(HTML_FILE)
    except KeyboardInterrupt:
        print("\nStopped watching.")

if __name__ == "__main__":
    main()
