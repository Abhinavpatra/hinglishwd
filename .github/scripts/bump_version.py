import re

with open('setup.py', 'r') as f:
    content = f.read()

def bump(match):
    major, minor, patch = match.group(1), match.group(2), match.group(3)
    new_patch = str(int(patch) + 1)
    return f'version="{major}.{minor}.{new_patch}"'

new_content = re.sub(r'version="(\d+)\.(\d+)\.(\d+)"', bump, content)

with open('setup.py', 'w') as f:
    f.write(new_content)

match = re.search(r'version="(\d+\.\d+\.\d+)"', new_content)
if match:
    print(f"Bumped version to {match.group(1)}")
