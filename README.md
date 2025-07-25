# 🕸️ Deep Web Scraper 🕵️‍♂️

A powerful Python-based scraper that explores an entire website — crawling, clicking, expanding, and extracting all meaningful content, even from dynamic elements like dropdowns, buttons, and AJAX-loaded sections.

### 🚀 Features

- ✅ Clicks through dropdowns, buttons, and expandable sections

- ✅ Handles JavaScript-heavy websites using Playwright

- ✅ Follows internal links recursively (site-wide crawl)

- ✅ Extracts all text content (headings, paragraphs, lists)

- ✅ Filters and avoids duplicate pages

- ✅ Optional delay to wait for AJAX content


### 🧰 Tech Stack

- 🐍 Python 3

- 🎭 Playwright for headless browser automation

- 🍜 BeautifulSoup (optional for advanced parsing)

- 📂 urlparse and urljoin for URL handling



```
git clone https://github.com/deepgupta06/deep-web-scraper.git
cd deep-web-scraper
pip install -r requirements.txt
playwright install
```

### 🧑‍💻 Usage
```
python main.py
```

Update the target URL in main.py:

```
url = "https://example.com"
result = deep_scrape(url, max_pages=50)
```

### 📄 Output

Scraped content is saved to:

```
scraped_content.txt
```
Each section is labeled by its source URL for traceability.

### ⚙️ Configuration

You can tweak the following:

| Config       | Center Aligned                         | 
|:-------------|:--------------------------------------:|
| max_pages    | Max number of pages to crawl           |
| timeout	   | Wait time for each page to load        |
| headless	   | Set False to see browser UI (debug)    |


### 🔍 Example Use Cases

- 🔎 Research & content analysis

- 🧠 Feed to LangChain + Ollama RAG pipeline

- 🤖 Dataset generation for fine-tuning models

- 📚 Competitive website analysis

### ⚠️ Ethical Use Disclaimer

Please respect robots.txt and avoid scraping websites without permission.
This tool is intended for ethical, educational, and personal use only.

### 🤝 Contributing

Got improvements or new features in mind?
Feel free to open an issue or submit a PR! 🎉

### 🧠 Author

Made with 💻 by [Deep Gupta]

🐦 @deepgupta06

