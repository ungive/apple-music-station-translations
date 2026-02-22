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
final_regex_escaped = ''.join(
    f'\\u{ord(c):04x}' if ord(c) > 0x7f else c
    for c in final_regex
)

with open('out/regex.txt', 'w', encoding='utf-8') as file:
    file.write(final_regex)

with open('out/regex-escaped.txt', 'w', encoding='utf-8') as file:
    file.write(final_regex_escaped)

with open('out/regex-string-escaped.txt', 'w', encoding='utf-8') as file:
    file.write(re.sub(r"\\(?!u[0-9A-Fa-f]{4})", r"\\\\", final_regex_escaped))

print(final_regex)
