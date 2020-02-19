"""This is assignment 04a
    wriiten by Haodong Wu 18/02/2020
"""
import requests
import json


def repository_get(user):
    response = requests.get('https://api.github.com/users/' + user + '/repos')
    json_str = response.text
    repositories = json.loads(json_str)
    summary = []
    for repository in repositories:
        number_of_commits = commit_get(user, repository['name'])
        summary.append((repository['name'], number_of_commits))
    print(summary)
    return summary
def commit_get(user, repository):
    response = requests.get('https://api.github.com/repos/' + user + '/' + repository +'/commits')
    json_str = response.text
    commits = json.loads(json_str)
    #print(f"Repo: {repository} Number of commits: {len(commits)}")
    return len(commits)

def main():
    for repository, number_of_commits in repository_get('richkempinski'):
        print(f"Repo: {repository} Number of commits: {number_of_commits}")



if __name__ == "__main__":
    main()