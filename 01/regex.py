import re

text_to_search = "abcdef...asdabcg"
pattern = re.compile(r"abc")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)