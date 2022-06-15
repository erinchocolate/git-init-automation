import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
access_token = os.getenv("GITHUB_ACCESSTOKEN")

# Pass the dir name created throught command line as repo name
reponame = sys.argv[1]


def create(reponame):
    user = Github(access_token).get_user()
    # Create a remote repo
    repo = user.create_repo(reponame)
    print(f"Succesfully created repository {reponame}")


if __name__ == "__main__":
    create(reponame)
