import requests 
import json 
 
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in" 
CATEGORY_ID = "category-slug"  # Replace with real ID 
 
def scrape_posts(from_date, to_date): 
    all_posts = [] 
    page = 0 
    while True: 
        page += 1 
        url = f"{BASE_URL}/c/tds/{CATEGORY_ID}.json?page={page}" 
        r = requests.get(url) 
        if not r.ok: break 
        topics = r.json().get("topic_list", {}).get("topics", []) 
        if not topics: break 
        for topic in topics: 
                post = { 
                    "id": topic["id"], 
                    "title": topic["title"], 
                    "url": f"{BASE_URL}/t/{topic['slug']}/{topic['id']}" 
                } 
                all_posts.append(post) 
    with open("discourse_posts.json", "w") as f: 
        json.dump(all_posts, f, indent=2) 
 
scrape_posts("2025-01-01", "2025-04-14") 
