import sys
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
access_token = os.getenv("GITHUB_ACCESSTOKEN")


def create():
    user = Github(login_or_token=access_token, base_url="https://github.com").get_user()
    repo = user.create_repo("test")


if __name__ == "__main__":
    create()
