import requests
import yaml
import os

# Sergio's ORCID ID
ORCID_ID = "0009-0009-4185-9405"
API_URL = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
HEADERS = {"Accept": "application/json"}

def fetch_works():
    print(f"Fetching ORCID data for {ORCID_ID}...")
    try:
        response = requests.get(API_URL, headers=HEADERS)
        if response.status_code!= 200:
            print(f"Error: Received status code {response.status_code}")
            return
            
        data = response.json()
        
        # FIX: Initialize empty list correctly
        works =
        
        # Check if 'group' exists
        if 'group' not in data:
            print("No 'group' key found in ORCID response.")
            return

        for group in data['group']:
            for summary in group.get('work-summary',):
                # Safely get title
                title = "Untitled"
                if summary.get('title') and summary['title'].get('title'):
                    title = summary['title']['title'].get('value', 'Untitled')
                
                # Safely get year
                year = "n.d."
                if summary.get('publication-date') and summary['publication-date'].get('year'):
                    year = summary['publication-date']['year'].get('value', 'n.d.')
                
                # Safely get URL
                url = ""
                if summary.get('url'):
                    url = summary['url'].get('value', "")
                
                # Safely get Journal
                journal = "Publication"
                if summary.get('journal-title'):
                    journal = summary['journal-title'].get('value', 'Publication')
                
                works.append({
                    "title": title,
                    "year": year,
                    "url": url,
                    "journal": journal
                })
        return works
    except Exception as e:
        print(f"Exception occurred: {e}")
        return

if __name__ == "__main__":
    works_list = fetch_works()
    
    # Ensure _data directory exists
    os.makedirs("_data", exist_ok=True)
    
    if works_list:
        with open("_data/publications.yml", "w", encoding="utf-8") as f:
            yaml.dump(works_list, f, allow_unicode=True)
        print(f"Successfully updated {len(works_list)} publications.")
    else:
        print("No publications found or error occurred.")
