from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
import time

visited = set()

def is_internal(url, base):
    return urlparse(url).netloc == urlparse(base).netloc

def scrape_page(page, base_url):
    content = ""
    
    # Expand dropdowns and clickables
    for el in page.query_selector_all("select, button, details"):
        try:
            el.click(timeout=1000)
            time.sleep(0.5)
        except:
            continue

    # Wait for AJAX
    page.wait_for_timeout(1000)

    # Extract all text
    body_text = page.inner_text("body")
    content += body_text + "\n"

    # Extract and return all internal links
    links = set()
    for a in page.query_selector_all("a"):
        href = a.get_attribute("href")
        if href:
            full_url = urljoin(base_url, href)
            if is_internal(full_url, base_url):
                links.add(full_url)

    return content, links

def deep_scrape(base_url, max_pages=50):
    all_data = ""
    to_visit = [base_url]
    count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        while to_visit and count < max_pages:
            url = to_visit.pop(0)
            if url in visited:
                continue
            visited.add(url)

            try:
                page.goto(url, timeout=30000, wait_until="domcontentloaded")
                page.wait_for_timeout(2000)  # optional delay for full rendering
                print(f"[+] Scraping: {url}")
                content, links = scrape_page(page, base_url)
                all_data += f"\n\n# URL: {url}\n{content}"
                to_visit.extend(links - visited)
                count += 1
            except Exception as e:
                print(f"[!] Failed to load {url}: {e}")
        
        browser.close()
    
    return all_data



if __name__ == "__main__":
    url = "https://themes-coder.net/html/groceries/android/index.html"
    result = deep_scrape(url, max_pages=20)

    with open("scraped_content.txt", "w", encoding="utf-8") as f:
        f.write(result)
