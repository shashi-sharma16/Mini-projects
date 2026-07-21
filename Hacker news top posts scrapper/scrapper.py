import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"


def fetch_top_posts():
    """Fetch the top 20 Hacker News posts."""
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")

    posts = []
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get("href" or "").strip()
        posts.append({"title": title, "url": url})

    return posts


def save_to_csv(posts):
    """Save scraped posts to a CSV file."""
    if not posts:
        print("Nothing to save.")
        return
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)

    print(f"✅ Saved Hacker News to {CSV_FILE}")



def main():
    print("Scraping the Hacker News homepage...")
    posts = fetch_top_posts()      
    print(f"Collected {len(posts)} posts.")
    save_to_csv(posts)


main()

