🕸️ Deep Web Scraper 🕵️‍♂️

A powerful Python-based scraper that explores an entire website — crawling, clicking, expanding, and extracting all meaningful content, even from dynamic elements like dropdowns, buttons, and AJAX-loaded sections.

🚀 Features

- ✅ Clicks through dropdowns, buttons, and expandable sections

✅ Handles JavaScript-heavy websites using Playwright
✅ Follows internal links recursively (site-wide crawl)
✅ Extracts all text content (headings, paragraphs, lists)
✅ Filters and avoids duplicate pages
✅ Optional delay to wait for AJAX content

🧰 Tech Stack
🐍 Python 3

🎭 Playwright for headless browser automation

🍜 BeautifulSoup (optional for advanced parsing)

📂 urlparse and urljoin for URL handling



```
git clone https://github.com/yourusername/deep-web-scraper.git
cd deep-web-scraper
pip install -r requirements.txt
playwright install
```