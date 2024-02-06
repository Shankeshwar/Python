import re

text = "The quick brown brown brown fox"
pattern = r"brown fox"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")