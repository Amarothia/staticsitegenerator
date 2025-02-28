import re

def extract_title(markdown: str):
    # Look for a line that starts with a single # followed by a space
    matches = re.search(r"^# (.+)$", markdown, re.MULTILINE)
    if matches:
        # Return the captured group (everything after "# ")
        return matches.group(1).strip()
    raise Exception("No title for the page.")