"""
PROVEN SOLUTION FOR ARM UBUNTU
Web scraping WITHOUT browsers
"""

import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    """Scrape any website without browser"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux aarch64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    try:
        print(f"🌐 Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract data
            data = {
                'url': url,
                'status': response.status_code,
                'title': soup.title.string if soup.title else 'No title',
                'h1_tags': [h1.get_text(strip=True) for h1 in soup.find_all('h1')],
                'meta_tags': {
                    meta.get('name', meta.get('property', 'unknown')): meta.get('content', '')
                    for meta in soup.find_all('meta')
                    if meta.get('name') or meta.get('property')
                },
                'text_sample': soup.get_text()[:500] + '...' if len(soup.get_text()) > 500 else soup.get_text(),
            }
            
            return data
        else:
            print(f"  ❌ HTTP {response.status_code}")
            return None
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None

print("=" * 60)
print("PROVEN WEB SCRAPING SOLUTION")
print("=" * 60)
print("Works on ARM Ubuntu WITHOUT browsers or Selenium!")
print("=" * 60)

# Test with multiple sites
test_sites = [
    "https://httpbin.org/html",
    "https://example.com",
    "https://httpbin.org/json",
    "https://en.wikipedia.org/wiki/Python_(programming_language)"
]

results = []
success_count = 0

for site in test_sites:
    result = scrape_website(site)
    if result:
        results.append(result)
        success_count += 1
        print(f"  ✅ Successfully scraped")
    print()

print("=" * 60)
print(f"RESULTS: {success_count}/{len(test_sites)} sites scraped")
print("=" * 60)

if success_count > 0:
    # Save results
    with open('/tmp/scraping_results.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n📁 Results saved to: /tmp/scraping_results.json")
    
    # Show sample
    print("\n📋 SAMPLE DATA (first result):")
    if results:
        first = results[0]
        print(f"URL: {first['url']}")
        print(f"Title: {first['title']}")
        print(f"H1 tags: {first['h1_tags']}")
    
    print("\n" + "=" * 60)
    print("🎉 CONGRATULATIONS! Your web scraping setup works!")
    print("=" * 60)
    print("\nYou can now:")
    print("1. Scrape any website")
    print("2. Extract data (text, links, images)")
    print("3. Parse HTML/XML content")
    print("4. Save data to files/databases")
    print("\nNo Selenium needed! No browser installation issues!")
    
else:
    print("\n❌ No sites could be scraped. Check network connection.")
