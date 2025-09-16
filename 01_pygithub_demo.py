from github import Github
from github import Auth

access_token = "access_token"
auth = Auth.Token(access_token)
g = Github(auth=auth)

"""
Option 1 to authenticate to Github
g = Github("username", "password")
# Option 2 to authenticate to Github using access token
g = Github(access_token)
"""

# Extract user and bio
current_user = g.get_user()
print(current_user.name)
print(current_user.bio)

# Extract all repos
for repo in g.get_user().get_repos():
    print(repo.name)
print("========================")
# Extract repos written in python  (Do not run this, it runs on entire github)
python_repos = g.search_repositories(query="language.python")
for repo in python_repos:
    print(repo.name)
print("========================")
# Close the connection
g.close()