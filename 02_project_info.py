from github import Github
from github import Auth
import pandas as pd 

access_token = "access_token"
auth = Auth.Token(access_token)

project_list = ['apache/any23', 'apache/dubbo', 'apache/calcite', 'apache/cassandra', 
                'apache/cxf', 'apache/flume', 'apache/groovy']
print(project_list)


def extract_project_info():
    df_project = pd.DataFrame()
    rows = []
    for project in project_list:
        g = Github(auth=auth)
        repo = g.get_repo(project)
        print(repo)
        PRs = repo.get_pulls(state='all')
        print(PRs)
        row = {
            'Project_ID': repo.id, 
            'Name': repo.name,
            'Full_name': repo.full_name,
            'Language': repo.language,
            'Forks': repo.forks_count,
            'Stars': repo.stargazers_count,
            'Watchers': repo.subscribers_count,
            'PRs_count': PRs.totalCount
        }
        rows.append(row)
    df_project = pd.DataFrame(rows)
    df_project.to_csv('project_dataset.csv', sep=',', encoding='utf-8', index=True)

extract_project_info()