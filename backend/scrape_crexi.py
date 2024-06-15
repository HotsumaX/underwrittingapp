import json
from playwright.sync_api import sync_playwright

def scrape_crexi_listing(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        
        # Increase timeout and wait for the property details to load
        try:
            page.wait_for_selector('body', timeout=90000)
            
            # Extract all text content
            content = page.inner_text('body')
            
            # Extract all visible elements and their inner texts
            elements = page.query_selector_all('*')
            element_texts = {}
            for element in elements:
                try:
                    element_texts[element.get_attribute('class')] = element.inner_text()
                except Exception:
                    pass
            
            # Save the extracted content to a JSON file
            data = {
                'content': content,
                'element_texts': element_texts
            }
            with open('crexi_listing.json', 'w') as f:
                json.dump(data, f, indent=4)

            print(f"Scraped data saved to crexi_listing.json")
        
        except Exception as e:
            print(f"Error waiting for page to load: {e}")
        
        finally:
            browser.close()

if __name__ == "__main__":
    scrape_crexi_listing('https://www.crexi.com/properties/1552847/colorado-982-s-sheridan-blvd')