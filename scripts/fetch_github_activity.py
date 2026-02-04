import os
import requests
import yaml

# Update with your GitHub username
GITHUB_USER = "sergio1817"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos?sort=updated&per_page=5"

HEADERS = {
    "Accept": "application/vnd.github+json",
}


def fetch_repos():
    response = requests.get(API_URL, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []
    return response.json()


def main():
    repos = fetch_repos()
    data = []
    for repo in repos:
        data.append(
            {
                "name": repo.get("name"),
                "url": repo.get("html_url"),
                "description": repo.get("description") or "",
                "updated": repo.get("updated_at", ""),
                "language": repo.get("language") or "",
            }
        )

    os.makedirs("_data", exist_ok=True)
    with open("_data/github.yml", "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)
    print(f"Saved {len(data)} repos to _data/github.yml")


if __name__ == "__main__":
    main()
