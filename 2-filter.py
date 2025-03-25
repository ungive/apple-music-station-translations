import json
import re
import codecs

USERNAME = 'Kamawanujp'
USERNAME_REGEX = '.+'

with open('out/station-translations-1.json', 'r') as file:
    translations = json.load(file)
    for t in translations:
        if USERNAME not in t['text']:
            raise ValueError('invalid')

regexes = set()
for t in translations:
    text: str = t['text']
    text = text.strip()
    text = text.replace(USERNAME, 'A' * 10)
    text = re.escape(text)
    regex = text.replace('A' * 10, USERNAME_REGEX)
    regexes.add(regex)

final_regex = '(' + '|'.join(sorted(regexes)) + ')'

with codecs.open('out/regex.txt', 'w', 'utf-8') as file:
    file.write(final_regex)

print(final_regex)
