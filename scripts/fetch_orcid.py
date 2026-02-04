
import requests
import yaml

ORCID_ID = "0009-0009-4185-9405"
API_URL = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
HEADERS = {"Accept": "application/json"}

def fetch_works():
    print(f"Fetching ORCID data for {ORCID_ID}...")
    try:
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        
        works =
        for group in data.get('group',):
            for summary in group.get('work-summary',):
                title = summary.get('title', {}).get('title', {}).get('value', 'Untitled')
                
                # Extract Year
                try:
                    year = summary.get('publication-date', {}).get('year', {}).get('value', 'n.d.')
                except:
                    year = 'n.d.'
                
                # Extract URL
                url = ""
                if summary.get('url'):
                    url = summary.get('url', {}).get('value', "")
                
                # Extract Journal
                journal = summary.get('journal-title', {}).get('value', 'Publication')
                
                works.append({
                    "title": title,
                    "year": year,
                    "url": url,
                    "journal": journal
                })
        return works
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

if __name__ == "__main__":
    works = fetch_works()
    if works:
        with open("_data/publications.yml", "w", encoding="utf-8") as f:
            yaml.dump(works, f, allow_unicode=True)
        print("Publications updated.")
    else:
        print("No publications found or error occurred.")
