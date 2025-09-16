from github import Github, RateLimitExceededException, BadCredentialsException
from github import BadAttributeException, GithubException, UnknownObjectException
from github import BadUserAgentException
from github import Auth
import pandas as pd 
import requests
import time 

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


def extract_project_info_exception_handle():
    df_project = pd.DataFrame()
    rows = []
    for project in project_list:
        print(project)
        while True: 
            try: 
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
            except RateLimitExceededException as e:
                print(e.status)
                print('Rate limit exceeded')
                time.sleep(300)
                continue
            except BadCredentialsException as e:
                print(e.status)
                print('Bad credentials exception')
                break
            except UnknownObjectException as e:
                print(e.status)
                print('Unknown object exception')
                break
            except GithubException as e:
                print(e.status)
                print('General exception')
                break
            except requests.exceptions.ConnectionError as e:
                print('Retries limit exceeded')
                print(str(e))
                time.sleep(10)
                continue
            except requests.exceptions.Timeout as e:
                print(str(e))
                print('Time out exception')
                time.sleep(10)
                continue
            break
    df_project = pd.DataFrame(rows)
    df_project.to_csv('project_dataset.csv', sep=',', encoding='utf-8', index=True)


# extract_project_info()
extract_project_info_exception_handle()