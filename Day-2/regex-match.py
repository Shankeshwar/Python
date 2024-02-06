import re

text = "word is quick"
pattern = "quick"

match = re.match(pattern, text)
if match:
    print(f"Match found:",{match.group()})
else:
    print("No match")