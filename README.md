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

The final regex to use is located in `out/regex.txt`

---

Source region-codes.json: https://gist.github.com/ssskip/5a94bfcd2835bf1dea52
