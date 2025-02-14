import requests
import sys

def fetch_commits(repo):
    url = f"https://api.github.com/repos/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch commits: {response.status_code} {response.text}")
        return
    
    commits = response.json()
    for commit in commits[:10]:  # Fetching latest 10 commits
        author = commit['commit']['author']['name']
        message = commit['commit']['message']
        print(f"Author: {author}\nMessage: {message}\n")

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "projnajit/SpringPractise"
    fetch_commits(repo)

    #hello_world
