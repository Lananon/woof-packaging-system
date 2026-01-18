import sys
from git import Repo

def main():
  repo_url = sys.argv[1]
  destination = "./REPO"

  Repo.clone_from(repo_url, destination)
  


if __name__ == "__main__":
  main()
