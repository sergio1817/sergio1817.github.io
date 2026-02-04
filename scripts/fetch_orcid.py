
import requests
import yaml
import os

# Sergio's ORCID ID
ORCID_ID = "0009-0009-4185-9405"
API_URL = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"

headers = {"Accept": "application/json"}

def fetch_works():
    print(f"Fetching data for ORCID: {ORCID_ID}")
    response = requests.get(API_URL, headers=headers)
    if response.status_code!= 200:
        print(f"Error: {response.status_code}")
        return
    
    data = response.json()
    works =
    
    # Parse the messy ORCID JSON structure
    for group in data.get('group',):
        for summary in group.get('work-summary',):
            title = summary.get('title', {}).get('title', {}).get('value', 'Untitled')
            year = "n.d."
            try:
                year = summary.get('publication-date', {}).get('year', {}).get('value', 'n.d.')
            except:
                pass
            
            # Get link if available
            url = ""
            if summary.get('url'):
                url = summary.get('url', {}).get('value', "")
                
            works.append({
                "title": title,
                "year": year,
                "url": url,
                "journal": summary.get('journal-title', {}).get('value', 'Publication')
            })
            
    return works

if __name__ == "__main__":
    works_list = fetch_works()
    
    # Save to _data/publications.yml
    output_path = "_data/publications.yml"
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(works_list, f, allow_unicode=True)
    
    print(f"Successfully saved {len(works_list)} publications to {output_path}")
