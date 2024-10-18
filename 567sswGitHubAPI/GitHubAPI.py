import requests
import json

def get_user_repos_and_commits(user_id):
    # Base URL for GitHub API to get user's repositories
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    
    # Make a GET request to retrieve the user's repositories
    response = requests.get(repos_url)
    
    # Check if the response status code is OK (200)
    if response.status_code == 200:
        # Parse the JSON response
        repos = response.json()
        
        # Iterate through the repositories and get the number of commits for each
        for repo in repos:
            repo_name = repo['name']
            commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
            
            # Make a GET request to retrieve commits for the current repository
            commits_response = requests.get(commits_url)
            
            if commits_response.status_code == 200:
                commits = commits_response.json()
                # Count the number of commits (length of the commits list)
                num_commits = len(commits)
                print(f"Repo: {repo_name} Number of commits: {num_commits}")
            else:
                print(f"Failed to retrieve commits for repo: {repo_name}")
    else:
        print(f"Failed to retrieve repositories for user: {user_id}")

# Example usage
get_user_repos_and_commits("richkempinski")
