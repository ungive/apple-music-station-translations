## Apple Music "Station" translations

Generates a regular expression for matching Apple Music Stations
which contain personal data of the Apple Music user.

Usage:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python 1-scrape.py
python 2-filter.py
g++ -o ./a.out test.cpp
python 3-test.py
```

- Scrapes all translations for Stations from localized Apple Music pages
- Filters out duplicates and creates a universal regular expression
- Compiles the test program (testing the regex using C++ regular expressions)
- Runs the C++ test program with all scraped strings to ensure the regex is ok

Output artifacts:

- `regex.txt`: The raw UTF-8 encoded regular expression
- `regex-escaped.txt`: The raw UTF-8 encoded regular expression with escaped Unicode sequences
- `regex-string-escaped.txt`: A UTF-8 encoded version of the regular expression with escaped Unicode sequences that can be used in a string variable in various programming languages, JSON and YAML

---

Source region-codes.json: https://gist.github.com/ssskip/5a94bfcd2835bf1dea52
