import re
import os
import time
import watch_resume

def get_pages():
    with open('resume.pdf', 'rb') as f:
        data = f.read()
    return len(re.findall(b'/Type\s*/Page[^s]', data))

watch_resume.compile_pdf()
time.sleep(1)
print("PAGES:", get_pages())
