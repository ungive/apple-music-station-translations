import json
from subprocess import Popen, PIPE

with open('out/station-translations-1.json', 'r') as file:
    translations = json.load(file)

for t in translations:
    text: str = t['text']
    text = text.strip()
    print(text, end=' ')
    process = Popen(["./a.out", text], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if exit_code != 0 or output != b'1':
        print('FAILED', exit_code, output)
        exit(-1)
    print('OK')

print('SUCCESS')
